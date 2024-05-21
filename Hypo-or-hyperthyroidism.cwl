cwlVersion: v1.0
steps:
  read-potential-cases-omop:
    run: read-potential-cases-omop.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule1
  hypo-or-hyperthyroidism---primary:
    run: hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule2
      potentialCases:
        id: potentialCases
        source: read-potential-cases-omop/output
  thyrotoxic-hypo-or-hyperthyroidism---primary:
    run: thyrotoxic-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule3
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism---primary/output
  chronic-hypo-or-hyperthyroidism---primary:
    run: chronic-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule4
      potentialCases:
        id: potentialCases
        source: thyrotoxic-hypo-or-hyperthyroidism---primary/output
  hypo-or-hyperthyroidism-acquired---primary:
    run: hypo-or-hyperthyroidism-acquired---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule5
      potentialCases:
        id: potentialCases
        source: chronic-hypo-or-hyperthyroidism---primary/output
  hypo-or-hyperthyroidism-graves'---primary:
    run: hypo-or-hyperthyroidism-graves'---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule6
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-acquired---primary/output
  hyperthyroidism---primary:
    run: hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule7
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-graves'---primary/output
  hypo-or-hyperthyroidism-basedow's---primary:
    run: hypo-or-hyperthyroidism-basedow's---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule8
      potentialCases:
        id: potentialCases
        source: hyperthyroidism---primary/output
  dysthyroid-hypo-or-hyperthyroidism---primary:
    run: dysthyroid-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule9
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-basedow's---primary/output
  hypo-or-hyperthyroidism-thyroiditis---primary:
    run: hypo-or-hyperthyroidism-thyroiditis---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule10
      potentialCases:
        id: potentialCases
        source: dysthyroid-hypo-or-hyperthyroidism---primary/output
  hypo-or-hyperthyroidism-myxoedema---primary:
    run: hypo-or-hyperthyroidism-myxoedema---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule11
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-thyroiditis---primary/output
  postablative-hypo-or-hyperthyroidism---primary:
    run: postablative-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule12
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-myxoedema---primary/output
  hypo-or-hyperthyroidism-autoimmune---primary:
    run: hypo-or-hyperthyroidism-autoimmune---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule13
      potentialCases:
        id: potentialCases
        source: postablative-hypo-or-hyperthyroidism---primary/output
  hypo-or-hyperthyroidism-letter---primary:
    run: hypo-or-hyperthyroidism-letter---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule14
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-autoimmune---primary/output
  hypo-or-hyperthyroidism-specified---primary:
    run: hypo-or-hyperthyroidism-specified---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule15
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-letter---primary/output
  hypo-or-hyperthyroidism-hashimoto's---primary:
    run: hypo-or-hyperthyroidism-hashimoto's---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule16
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-specified---primary/output
  hypo-or-hyperthyroidism-hypothyroidism---primary:
    run: hypo-or-hyperthyroidism-hypothyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule17
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-hashimoto's---primary/output
  myasthenic-hypo-or-hyperthyroidism---primary:
    run: myasthenic-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule18
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-hypothyroidism---primary/output
  myopathy-hypo-or-hyperthyroidism---primary:
    run: myopathy-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule19
      potentialCases:
        id: potentialCases
        source: myasthenic-hypo-or-hyperthyroidism---primary/output
  iatrogenic-hypo-or-hyperthyroidism---primary:
    run: iatrogenic-hypo-or-hyperthyroidism---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule20
      potentialCases:
        id: potentialCases
        source: myopathy-hypo-or-hyperthyroidism---primary/output
  hypo-or-hyperthyroidism-deficiency---primary:
    run: hypo-or-hyperthyroidism-deficiency---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule21
      potentialCases:
        id: potentialCases
        source: iatrogenic-hypo-or-hyperthyroidism---primary/output
  hypo---primary:
    run: hypo---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule22
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-deficiency---primary/output
  hypo-or-hyperthyroidism-history---primary:
    run: hypo-or-hyperthyroidism-history---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule23
      potentialCases:
        id: potentialCases
        source: hypo---primary/output
  output-cases:
    run: output-cases.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule24
      potentialCases:
        id: potentialCases
        source: hypo-or-hyperthyroidism-history---primary/output
class: Workflow
inputs:
  inputModule1:
    id: inputModule1
    doc: Js implementation unit
    type: File
  inputModule2:
    id: inputModule2
    doc: Python implementation unit
    type: File
  inputModule3:
    id: inputModule3
    doc: Python implementation unit
    type: File
  inputModule4:
    id: inputModule4
    doc: Python implementation unit
    type: File
  inputModule5:
    id: inputModule5
    doc: Python implementation unit
    type: File
  inputModule6:
    id: inputModule6
    doc: Python implementation unit
    type: File
  inputModule7:
    id: inputModule7
    doc: Python implementation unit
    type: File
  inputModule8:
    id: inputModule8
    doc: Python implementation unit
    type: File
  inputModule9:
    id: inputModule9
    doc: Python implementation unit
    type: File
  inputModule10:
    id: inputModule10
    doc: Python implementation unit
    type: File
  inputModule11:
    id: inputModule11
    doc: Python implementation unit
    type: File
  inputModule12:
    id: inputModule12
    doc: Python implementation unit
    type: File
  inputModule13:
    id: inputModule13
    doc: Python implementation unit
    type: File
  inputModule14:
    id: inputModule14
    doc: Python implementation unit
    type: File
  inputModule15:
    id: inputModule15
    doc: Python implementation unit
    type: File
  inputModule16:
    id: inputModule16
    doc: Python implementation unit
    type: File
  inputModule17:
    id: inputModule17
    doc: Python implementation unit
    type: File
  inputModule18:
    id: inputModule18
    doc: Python implementation unit
    type: File
  inputModule19:
    id: inputModule19
    doc: Python implementation unit
    type: File
  inputModule20:
    id: inputModule20
    doc: Python implementation unit
    type: File
  inputModule21:
    id: inputModule21
    doc: Python implementation unit
    type: File
  inputModule22:
    id: inputModule22
    doc: Python implementation unit
    type: File
  inputModule23:
    id: inputModule23
    doc: Python implementation unit
    type: File
  inputModule24:
    id: inputModule24
    doc: Python implementation unit
    type: File
outputs:
  cases:
    id: cases
    type: File
    outputSource: output-cases/output
    outputBinding:
      glob: '*.csv'
requirements:
  SubworkflowFeatureRequirement: {}
