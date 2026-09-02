# ML, VLA, and robotics review gates

## Contents

- [Shared gate pattern](#shared-gate-pattern)
- [Data leakage and contamination](#data-leakage-and-contamination)
- [Matched comparisons](#matched-comparisons)
- [Replication and statistical independence](#replication-and-statistical-independence)
- [Ablations and attribution](#ablations-and-attribution)
- [Generalization and transfer](#generalization-and-transfer)
- [Robotics and embodied deployment](#robotics-and-embodied-deployment)
- [Failures and safety](#failures-and-safety)
- [Reproducibility](#reproducibility)

Use these gates only after the shared manuscript fact base is clear. They are claim-dependent
stress tests inside `robotics-reviewer`. They do not create specialist reviewer identities or
replace verified target-venue criteria.

Convert supported diagnostics into normal reviewer prose. Do not expose this file's gate names or
routing structure in the final report.

## Shared gate pattern

For each central claim, identify:

- the exact scope of the contribution;
- the evidence chain needed to support it;
- the unit of generalization, such as sample, scene, episode, task, dataset, robot, embodiment, or
  deployment site;
- assumptions, controls, uncertainty, and plausible alternative explanations;
- whether supplied evidence directly demonstrates the claim or only a narrower result;
- what evidence, analysis, disclosure, or claim moderation would resolve the concern.

A gate raises no concern merely because the manuscript packet does not show the information. Mark
it not assessable unless the missing item is verifiably required for a central claim or by the
current venue policy.

## Data leakage and contamination

Stress-test:

- whether train, validation, and test partitions are independent at the correct grouping level,
  including subjects, scenes, trajectories, episodes, tasks, environments, time, or data source;
- whether preprocessing, normalization, feature construction, filtering, prompt selection,
  checkpoint selection, or hyperparameter tuning uses test information;
- whether benchmark test feedback, public leaderboards, repeated submissions, or manual failure
  inspection influenced method selection;
- whether pretrained models may contain benchmark, evaluation, instruction, image, video, or web
  data overlap and whether the paper measures or bounds that risk;
- whether demonstrations, synthetic augmentation, retrieval corpora, robot logs, or foundation
  model pretraining leak evaluation targets.

Typical resolution direction: grouped or temporally blocked splits, untouched final evaluation,
contamination analysis, pretraining disclosure, sensitivity tests, or narrower claims.

## Matched comparisons

Stress-test:

- whether baselines use matched training data, supervision, backbone, initialization, pretraining,
  input modalities, observation and action spaces, compute, tuning effort, and evaluation budget;
- whether baseline implementations are current, correctly configured, and run under the same
  simulator, robot, sensor, task, and termination conditions;
- whether inference-time resources such as samples, planning horizon, retrieval, test-time
  adaptation, privileged state, human intervention, or external APIs are counted;
- whether comparisons separate method improvement from scale, proprietary data, extra labels,
  stronger perception, or larger hardware;
- whether metric definitions, success criteria, exclusions, and confidence intervals are
  identical across methods.

Typical resolution direction: controlled re-runs, resource-normalized comparisons, transparent
advantage accounting, or qualified conclusions.

## Replication and statistical independence

Stress-test:

- the number of independent training seeds and whether variability across runs is reported;
- whether evaluations are paired on the same tasks, initial states, scenes, or episodes when that
  design improves sensitivity;
- whether episodes, frames, time steps, grasps, or repeated trials are incorrectly treated as
  independent when they share a seed, scene, object, robot, operator, or deployment;
- whether the reported sample size distinguishes training runs, evaluation seeds, environments,
  objects, tasks, robots, users, and individual attempts;
- whether confidence intervals or hypothesis tests respect clustering, repeated measures, and
  multiple comparisons;
- whether stochastic policies and simulators are evaluated with enough independent units to
  support headline differences.

Typical resolution direction: define the unit of analysis, report seed-level and grouped
uncertainty, use paired or hierarchical analysis where appropriate, and moderate claims when
independent replication is limited.

## Ablations and attribution

Stress-test:

- whether each ablation changes one interpretable factor while holding data, compute, backbone,
  training schedule, evaluation protocol, and tuning budget fixed;
- whether architecture, objective, data mixture, scale, prompting, augmentation, and system
  components are disentangled;
- whether component removal creates an invalid or unfairly under-tuned baseline;
- whether interaction effects or alternative explanations are tested when components are claimed
  to be independently necessary;
- whether post hoc qualitative examples are presented as causal evidence for mechanism.

Typical resolution direction: controlled ablations, matched retraining, factorial or sensitivity
analysis, and claims limited to what the intervention actually isolates.

## Generalization and transfer

Stress-test:

- whether claimed OOD performance is genuinely outside training and tuning distributions;
- whether evaluation covers unseen objects, tasks, instructions, scenes, domains, viewpoints,
  languages, users, dynamics, or environment layouts at the claimed scope;
- whether cross-dataset results control annotation, label, sensor, and metric differences;
- whether cross-robot or cross-embodiment claims vary morphology, kinematics, action space,
  sensing, calibration, and controller interfaces rather than only cosmetic conditions;
- whether adaptation data, demonstrations, fine-tuning, calibration, or test-time interaction are
  disclosed and counted;
- whether broad generalization claims rest on cherry-picked tasks or a single favorable benchmark.

Typical resolution direction: held-out groups, leave-domain-out evaluation, cross-embodiment
tests, explicit adaptation budgets, negative results, or narrower scope.

## Robotics and embodied deployment

Stress-test:

- whether simulation, offline replay, hardware-in-the-loop, teleoperation, and autonomous
  real-world trials are clearly distinguished;
- whether sim-to-real claims include unseen real-world evidence and explain calibration, domain
  randomization, adaptation, and residual reality gap;
- whether end-to-end latency includes perception, model inference, planning, communication,
  safety filters, and actuation rather than model inference alone;
- whether control frequency, sensor rate, synchronization, jitter, dropped frames, compute,
  memory, energy, and hardware are reported at deployment settings;
- whether privileged simulator state, external tracking, resets, object placement, operator
  selection, or human interventions affect success;
- whether evaluation covers realistic operating envelopes, task duration, recovery, wear,
  calibration drift, and environmental variation;
- whether success rate definitions, termination criteria, retry policies, and intervention rules
  match the deployment claim.

Typical resolution direction: end-to-end real-system measurements, autonomous trial accounting,
matched hardware tests, intervention-normalized metrics, operating-envelope evaluation, and
carefully bounded deployment claims.

## Failures and safety

Stress-test:

- whether failures are categorized by perception, language grounding, planning, control,
  embodiment, hardware, environment, operator, or safety intervention;
- whether aggregate success rates conceal rare but consequential failure modes;
- whether recovery, abstention, fallback, reset, emergency stop, collision, force, workspace,
  privacy, and human-proximity behavior are reported when relevant;
- whether safety filters change task success, latency, or comparison fairness;
- whether evaluation exposes the system to plausible edge cases without creating unjustified
  real-world risk;
- whether claims about robustness or safe deployment exceed the tested conditions.

Typical resolution direction: failure taxonomy with denominators, severity-aware metrics,
intervention and near-miss reporting, bounded stress tests, recovery evaluation, and moderated
safety claims.

## Reproducibility

Stress-test:

- availability or precise specification of code, data, checkpoints, prompts, templates, model
  versions, preprocessing, train and evaluation splits, hyperparameters, and random seeds;
- simulator, robot, sensor, firmware, driver, middleware, dependency, and hardware versions;
- training compute, inference hardware, runtime flags, decoding or sampling settings, and external
  services;
- exact task definitions, reset and termination rules, success criteria, exclusions, human
  intervention policy, and evaluation scripts;
- whether proprietary models or datasets leave enough information for independent scrutiny or a
  defensible reproducibility boundary;
- whether public artifacts reproduce the reported protocol rather than only a demo path.

Typical resolution direction: release or archive artifacts, add environment and protocol
specifications, document unavailable dependencies, and separate reproducible from non-reproducible
claims.
