class StructuredNLResult(BaseModel):
    explanation: str
    decision1: Literal[
    "Globally, _ABSTRACT_VAR1_",
    "Before bool_exp2, _ABSTRACT_VAR1_",
    "After bool_exp1, _ABSTRACT_VAR1_",
    "Between bool_exp1 and bool_exp2, _ABSTRACT_VAR1_",
    "After bool_exp1 until bool_exp2, _ABSTRACT_VAR1_",
    ]
    bool_exp1: str
    bool_exp2: str

    decision2: Literal['it is never the case that bool_exp3 holds',
 'it is never the case that bool_exp3 holds within N_DURATION1 time units',
 'it is never the case that bool_exp3 holds after N_DURATION0 time units',
 'it is never the case that bool_exp3 holds between N_DURATION0 and N_DURATION1 time units',
 'it is always the case that bool_exp3 holds',
 'it is always the case that bool_exp3 holds within N_DURATION1 time units',
 'it is always the case that bool_exp3 holds after N_DURATION0 time units',
 'it is always the case that bool_exp3 holds between N_DURATION0 and N_DURATION1 time units',
 'bool_exp3 eventually holds',
 'bool_exp3 eventually holds within N_DURATION1 time units',
 'bool_exp3 eventually holds after N_DURATION0 time units',
 'bool_exp3 eventually holds between N_DURATION0 and N_DURATION1 time units',
 'once bool_exp3 becomes satisfied it remains so for at least N_DURATION1 time units',
 'once bool_exp3 becomes satisfied it remains so for less than N_DURATION1 time units',
 'bool_exp3 holds repeatedly every N_DURATION1 time units',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 has occurred between N_DURATION0 and N_DURATION1 time units before bool_exp3 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 has occurred before bool_exp3 holds',
 'bool_exp3 holds without interruption until bool_exp4 holds',
 'bool_exp3 holds without interruption until bool_exp4 holds within N_DURATION1 time units',
 'bool_exp3 holds without interruption until bool_exp4 holds after N_DURATION0 time units',
 'bool_exp3 holds without interruption until bool_exp4 holds between N_DURATION0 and N_DURATION1 time units',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds without bool_cnt_exp3 holding in between',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds within N_DURATION1 time units',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds within N_DURATION1 time units without bool_cnt_exp3 holding in between',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds after N_DURATION0 time units',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds after N_DURATION0 time units without bool_cnt_exp3 holding in between',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds between N_DURATION0 and N_DURATION1 time units',
 'if bool_exp3 has occurred, then in response bool_exp4 eventually holds between N_DURATION0 and N_DURATION1 time units without bool_cnt_exp3 holding in between',
 'if bool_exp3 has occurred, then in response bool_exp4 holds continually',
 'if bool_exp3 has occurred, then in response bool_exp4 holds continually within N_DURATION1 time units',
 'if bool_exp3 has occurred, then in response bool_exp4 holds continually after N_DURATION0 time units',
 'if bool_exp3 has occurred, then in response bool_exp4 holds continually between N_DURATION0 and N_DURATION1 time units',
 'if bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units hold, then it must have been the case that bool_exp3 has occurred between N_DURATION0 and N_DURATION1 time units before bool_exp4 holds',
 'if bool_exp4 and afterwards bool_exp5 hold, then it must have been the case that bool_exp3 has occurred before bool_exp4 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units have occurred between N_DURATION0 and N_DURATION1 time units before bool_exp3 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 have occurred before bool_exp3 holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 eventually holds',
 'if bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units hold, then it must have been the case that bool_exp3 has occurred between N_DURATION0 and N_DURATION1 time units before bool_exp4 holds',
 'if bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 hold, then it must have been the case that bool_exp3 has occurred before bool_exp4 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units have occurred between N_DURATION0 and N_DURATION1 time units before bool_exp3 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 have occurred before bool_exp3 holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 eventually holds',
 'if bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units and afterwards bool_exp7 within N_DURATION7 time units hold, then it must have been the case that bool_exp3 has occurred between N_DURATION0 and N_DURATION1 time units before bool_exp4 holds',
 'if bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 and afterwards bool_exp7 hold, then it must have been the case that bool_exp3 has occurred before bool_exp4 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units and afterwards bool_exp7 within N_DURATION7 time units have occurred between N_DURATION0 and N_DURATION1 time units before bool_exp3 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 and afterwards bool_exp7 have occurred before bool_exp3 holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between followed by bool_exp7 within N_DURATION7 time units without bool_cnt_exp6 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units followed by bool_exp7 within N_DURATION7 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between followed by bool_exp7 without bool_cnt_exp6 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 followed by bool_exp7 eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between followed by bool_exp7 within N_DURATION7 time units without bool_cnt_exp6 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units followed by bool_exp7 within N_DURATION7 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between followed by bool_exp7 without bool_cnt_exp6 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 followed by bool_exp7 eventually holds',
 'if bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units and afterwards bool_exp7 within N_DURATION7 time units and afterwards bool_exp8 within N_DURATION9 time units hold, then it must have been the case that bool_exp3 has occurred between N_DURATION0 and N_DURATION1 time units before bool_exp4 holds',
 'if bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 and afterwards bool_exp7 and afterwards bool_exp8 hold, then it must have been the case that bool_exp3 has occurred before bool_exp4 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units and afterwards bool_exp7 within N_DURATION7 time units and afterwards bool_exp8 within N_DURATION9 time units have occurred between N_DURATION0 and N_DURATION1 time units before bool_exp3 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 and afterwards bool_exp7 and afterwards bool_exp8 have occurred before bool_exp3 holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between followed by bool_exp7 within N_DURATION7 time units without bool_cnt_exp6 holding in between followed by bool_exp8 within N_DURATION9 time units without bool_cnt_exp7 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units followed by bool_exp7 within N_DURATION7 time units followed by bool_exp8 within N_DURATION9 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between followed by bool_exp7 without bool_cnt_exp6 holding in between followed by bool_exp8 without bool_cnt_exp7 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 followed by bool_exp7 followed by bool_exp8 eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between followed by bool_exp7 within N_DURATION7 time units without bool_cnt_exp6 holding in between followed by bool_exp8 within N_DURATION9 time units without bool_cnt_exp7 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units followed by bool_exp7 within N_DURATION7 time units followed by bool_exp8 within N_DURATION9 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between followed by bool_exp7 without bool_cnt_exp6 holding in between followed by bool_exp8 without bool_cnt_exp7 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 followed by bool_exp7 followed by bool_exp8 eventually holds',
 'if bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units and afterwards bool_exp7 within N_DURATION7 time units and afterwards bool_exp8 within N_DURATION9 time units and afterwards bool_exp9 within N_DURATION11 time units hold, then it must have been the case that bool_exp3 has occurred between N_DURATION0 and N_DURATION1 time units before bool_exp4 holds',
 'if bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 and afterwards bool_exp7 and afterwards bool_exp8 and afterwards bool_exp9 hold, then it must have been the case that bool_exp3 has occurred before bool_exp4 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 within N_DURATION3 time units and afterwards bool_exp6 within N_DURATION5 time units and afterwards bool_exp7 within N_DURATION7 time units and afterwards bool_exp8 within N_DURATION9 time units and afterwards bool_exp9 within N_DURATION11 time units have occurred between N_DURATION0 and N_DURATION1 time units before bool_exp3 holds',
 'if bool_exp3 holds, then it must have been the case that bool_exp4 and afterwards bool_exp5 and afterwards bool_exp6 and afterwards bool_exp7 and afterwards bool_exp8 and afterwards bool_exp9 have occurred before bool_exp3 holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between followed by bool_exp7 within N_DURATION7 time units without bool_cnt_exp6 holding in between followed by bool_exp8 within N_DURATION9 time units without bool_cnt_exp7 holding in between followed by bool_exp9 within N_DURATION11 time units without bool_cnt_exp8 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units followed by bool_exp7 within N_DURATION7 time units followed by bool_exp8 within N_DURATION9 time units followed by bool_exp9 within N_DURATION11 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between followed by bool_exp7 without bool_cnt_exp6 holding in between followed by bool_exp8 without bool_cnt_exp7 holding in between followed by bool_exp9 without bool_cnt_exp8 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 followed by bool_exp7 followed by bool_exp8 followed by bool_exp9 eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 within N_DURATION3 time units without bool_cnt_exp4 holding in between followed by bool_exp6 within N_DURATION5 time units without bool_cnt_exp5 holding in between followed by bool_exp7 within N_DURATION7 time units without bool_cnt_exp6 holding in between followed by bool_exp8 within N_DURATION9 time units without bool_cnt_exp7 holding in between followed by bool_exp9 within N_DURATION11 time units without bool_cnt_exp8 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response within N_DURATION1 time units bool_exp4 followed by bool_exp5 within N_DURATION3 time units followed by bool_exp6 within N_DURATION5 time units followed by bool_exp7 within N_DURATION7 time units followed by bool_exp8 within N_DURATION9 time units followed by bool_exp9 within N_DURATION11 time units eventually holds',
 'if bool_exp3 has occurred, then in response without bool_cnt_exp3 holding in between bool_exp4 followed by bool_exp5 without bool_cnt_exp4 holding in between followed by bool_exp6 without bool_cnt_exp5 holding in between followed by bool_exp7 without bool_cnt_exp6 holding in between followed by bool_exp8 without bool_cnt_exp7 holding in between followed by bool_exp9 without bool_cnt_exp8 holding in between eventually holds',
 'if bool_exp3 has occurred, then in response bool_exp4 followed by bool_exp5 followed by bool_exp6 followed by bool_exp7 followed by bool_exp8 followed by bool_exp9 eventually holds']
    
    bool_exp3: str
    bool_exp4: str
    bool_exp5: str
    bool_exp6: str
    bool_exp7: str
    bool_exp8: str
    bool_exp9: str
    bool_cnt_exp3: str
    bool_cnt_exp4: str
    bool_cnt_exp5: str
    bool_cnt_exp6: str
    bool_cnt_exp7: str
    bool_cnt_exp8: str
    N_DURATION0: Optional[int]
    N_DURATION1: Optional[int]
    N_DURATION2: Optional[int]
    N_DURATION3: Optional[int]
    N_DURATION4: Optional[int]
    N_DURATION5: Optional[int]
    N_DURATION6: Optional[int]
    N_DURATION7: Optional[int]
    N_DURATION8: Optional[int]
    N_DURATION9: Optional[int]
    N_DURATION10: Optional[int]
    N_DURATION11: Optional[int]
    decision1_substring: str
    decision2_substring: str