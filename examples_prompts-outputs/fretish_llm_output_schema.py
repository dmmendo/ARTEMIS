class StructuredNLResult(BaseModel):
    explanation: str
    decision1: Literal[
        "while bool_exp1, _ABSTRACT_VAR1_", 
        "only while bool_exp1, _ABSTRACT_VAR1_",
        "before bool_exp1, _ABSTRACT_VAR1_",
        "only before bool_exp1, _ABSTRACT_VAR1_",
        "after bool_exp1, _ABSTRACT_VAR1_",
        "only after bool_exp1, _ABSTRACT_VAR1_",
        "whenever bool_exp1, _ABSTRACT_VAR1_",
        "upon bool_exp1, _ABSTRACT_VAR1_",
        "_ABSTRACT_VAR1_"
    ]
    bool_exp1: str
    decision2: Literal[
        "whenever bool_exp2, _ABSTRACT_VAR2_",
        "upon bool_exp2, _ABSTRACT_VAR2_",
        "_ABSTRACT_VAR2_"
    ]
    bool_exp2: str
    decision3: Literal[
        'immediately satisfy bool_exp3',
        'within N_DURATION ticks satisfy bool_exp3',
        'after N_DURATION ticks satisfy bool_exp3',
        'until bool_exp4, satisfy bool_exp3',
        'always satisfy bool_exp3',
        'never satisfy bool_exp3',
        'at the next timepoint satisfy bool_exp3',
        'eventually satisfy bool_exp3',
        'for N_DURATION ticks satisfy bool_exp3',
        'before bool_exp4, satisfy bool_exp3'
    ]
    bool_exp3: str
    bool_exp4: str
    N_DURATION: Optional[int]
    decision1_substring: str
    decision2_substring: str
    decision3_substring: str