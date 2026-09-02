# Robotics, ML, CV, and VLA publication profile

Use this reference to convert technical claims into the evidence and reporting
details expected for robotics and learning-system papers. It is not a source of
venue-specific formatting rules.

## Claim-to-evidence routing

- **Algorithmic improvement:** name the task, dataset or environment, metric,
  comparator, shared protocol, uncertainty across runs, and the ablation that
  isolates the claimed cause.
- **Robotic capability:** define the success criterion and evaluation unit;
  distinguish trials, episodes, scenes, objects, tasks, robot instances, and
  seeds. Report failures and human interventions rather than only successful
  demonstrations.
- **Generalization:** say exactly which axis is held out—object, scene, task,
  embodiment, language, domain, or environment—and prevent leakage across the
  corresponding train/validation/test split.
- **Sim-to-real or deployment:** separate simulation evidence from physical
  trials. Report platform, sensors, control frequency, latency, compute,
  calibration assumptions, safety constraints, and recovery behavior when they
  materially bound the claim.
- **VLA or multimodal system:** identify the vision, language, and action data
  provenance; policy interface; prompt or instruction protocol; action horizon;
  and whether evaluation measures perception, planning, control, or the full
  closed loop.
- **Efficiency or practicality:** report the relevant training and inference
  resources, runtime or throughput, memory, and any preprocessing or external
  service excluded from the headline number.

## Fair-comparison and reproducibility checks

- Compare methods under aligned data, splits, backbone or model scale, tuning
  budget, pretrained resources, sensors, and evaluation protocol. Disclose
  unavoidable mismatches instead of calling the comparison controlled.
- Distinguish independent runs from repeated measurements within one run. Do
  not treat frames or steps from the same episode as independent samples.
- Tie each ablation to one design claim; a component removal alone does not
  establish mechanism if it also changes capacity, data, or compute.
- Keep benchmark scores, real-world demonstrations, qualitative examples, and
  safety claims in their proper evidential roles. One does not silently stand
  in for another.
- Report enough implementation and evaluation detail to reproduce the result,
  while respecting the selected venue's current anonymity and artifact rules.

## Boundary discipline

State where the system stops working: distribution shift, unseen embodiments,
long-horizon compounding error, sensor degradation, latency, contact dynamics,
operator intervention, or unsafe states. Mention only boundaries supported by
the supplied evidence; use explicit placeholders for unmeasured ones.
