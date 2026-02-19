This README provides instructions on how to run ARTEMIS code and an overview of the codebase used for the implementation and evaluation of ARTEMIS and the baselines. We provide jupyter notebooks to conveniently run experiments in the paper and view the results. The jupyter notebook contain further instructions for running code.

## Additional paper details
ARTEMIS_appendix.pdf - We provide additional details on how ARTEMIS generates proxies

## Installation instructions
When prompted, enter "y" to agree to installation
1. install conda https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html
2. install nuXmv https://nuxmv.fbk.eu/download.html
3. install Python 3.9.21
    conda create -n myenv python=3.9
    conda activate myenv
4. install Spot for Python
    conda install conda-forge::spot
5. install python packages
    pip install notebook tqdm numpy pandas matplotlib openpyxl==3.1.5 openai==1.82.0 google-genai==1.16.1


## experiment scripts
To conveniently run the code, we highly recommend using one of the following jupyter notebooks:
Plot_results.ipynb - jupyter notebook which loads the accuracy and distinguishing trace generation results, and plots the figures in the paper
run_llm.ipynb - jupyter notebook which prompts LLMs to generate specifications on the benchmarks (requires Gemini API key)
compute_accuracy_metrics.ipynb  - jupyter notebook that loads the LLM-generated specifications and computes the translation accuracy
ProxyGenTest.ipynb - jupyter notebook that generates the proxies for FRETish and PSP used in ARTEMIS's distinguishing trace generation
run_dist_trace.ipynb - jupyter notebook that runs distinguishing trace generation experiments with LTLTalk and ARTEMIS

You should open the notebooks on a jupyter notebook server:
    jupyter notebook

Then copy and paste the printed link into a web browser.
Use the jupyter interface to find the notebook .ipynb file and double click to open it

## Examples
In the examples_prompt-outputs directory, contains example prompts nd outputs, including:
example_ARTEMIS_prompt.txt - an example of ARTEMIS LLM prompt using FRETish
example_ARTEMIS_output.txt - an example LLM output using ARTEMIS prompt using FRETish
example_directTL-t_prompt.txt - an example of directTL-t LLM prompt
example_directTL_prompt.txt - an example of directTL LLM prompt
fretish_llm_output_schema.py - contains the JSON schema used for generating FRETish with ARTEMIS
psp_llm_output_schema.py - contains the JSON schema used for generating PSP with ARTEMIS

## Benchmarks
The benchmarks (Ventilator, LMCPS, Robotics, Thales, DeepSTL) can be viewed in the benchmarks directory

## Evaluation Data
fretish_results and PSP_results contain the data collected from running the experiements in the evaluation.

## Code Structure
Core functionality
dist_trace.py - defines distinguishing trace generation of ARTEMIS and LTLTalk
nl2structnl_fretish.py - defines LLM prompts for ARTEMIS with FRETish IR
nl2structnl_PSP.py - defines LLM prompts for ARTEMIS with PSP IR
nl2structnl.py - helper functions for ARTEMIS's LLM prompts
proxy_gen.py - defines function for proxy generation for distinguishing trace generation

Baselines
deepstl.py - Defines LLM prompts for DeepSTL (FT)
nl2ltl.py - Defines LLM prompt for directTL and directTL-t
nl2spec.py - Defines LLM prompt for nl2spec
NL2TL.py - Defines LLM prompt for NL2TL+ and NL2TL+ (FT)
SynthTL.py - Defines LLM prompt for SynthTL

Utilities
automaton_utils.py - helper functions to manipulate automata
batch_check.py - Defines interface for dispatching model checker queries to NuSMV and Spot
data_loader.py - Defines helper functions to load in benchmarks and evaluation results
fret_utils.py - Defines helper functions to get LTL templates from FRET
llm_prompt.py - Defines the interface for querying LLMs (gemini and GPT)
metrics.py - Defines functions to compute accuracy for the evaluation
nusmv_utils.py - Defines functions to call NuXmv LTL model checker
spot_utils.py - Defines functions to call Spot LTL model checker

## Structured NL Templates
FRETish and PSP templates can be viewed in ./metadata/fretish_structnl_to_ltl_dict.json and ./metadata/psp_dict.json, respectively.

## Fine-tuning dataset
./finetuning_dataset/ contains the dataset used to fine-tune gemini-2.5-flash in our experiments
