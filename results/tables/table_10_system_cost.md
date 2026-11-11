**Table X. Computational cost of each component. Training times were measured on a single CPU core and are not a hardware benchmark of a deployed system.**

| Component                                       | Cost measure              |   Nominal model value |   Measured on this machine | Note                                     |
|:------------------------------------------------|:--------------------------|----------------------:|---------------------------:|:-----------------------------------------|
| policy: centralized_constrained                 | milliseconds per decision |                 1.036 |                     0.0081 | nominal values are simulator assumptions |
| policy: centralized_utility_max                 | milliseconds per decision |                 1.098 |                     0.0097 | nominal values are simulator assumptions |
| policy: decentralized_constrained               | milliseconds per decision |                 1.042 |                     0.0084 | nominal values are simulator assumptions |
| policy: decentralized_constrained_no_abstention | milliseconds per decision |                 1.156 |                     0.0079 | nominal values are simulator assumptions |
| policy: decentralized_utility_max               | milliseconds per decision |                 0.911 |                     0.0073 | nominal values are simulator assumptions |
| policy: rule_based_legacy                       | milliseconds per decision |                 0.4   |                     0.0135 | nominal values are simulator assumptions |
| fault model: dyhgt_marl                         | seconds to fit one seed   |                       |                   145.2    | single CPU core, no GPU                  |
| fault model: hist_gradient_boosting             | seconds to fit one seed   |                       |                     0.7    | single CPU core, no GPU                  |
| fault model: logistic_regression                | seconds to fit one seed   |                       |                     0.1    | single CPU core, no GPU                  |
| fault model: mlp                                | seconds to fit one seed   |                       |                     2.7    | single CPU core, no GPU                  |
| fault model: random_forest                      | seconds to fit one seed   |                       |                    15.1    | single CPU core, no GPU                  |
| fault model: random_forest_graph_features       | seconds to fit one seed   |                       |                    32.8    | single CPU core, no GPU                  |
| forecast model: dcrnn                           | seconds to fit one seed   |                       |                    23.1    | single CPU core, no GPU                  |
| forecast model: dyhgt                           | seconds to fit one seed   |                       |                   273      | single CPU core, no GPU                  |
| forecast model: gru                             | seconds to fit one seed   |                       |                    30      | single CPU core, no GPU                  |
| forecast model: ha                              | seconds to fit one seed   |                       |                     0      | single CPU core, no GPU                  |
| forecast model: ridge                           | seconds to fit one seed   |                       |                     0      | single CPU core, no GPU                  |
| forecast model: stgcn                           | seconds to fit one seed   |                       |                    29      | single CPU core, no GPU                  |
| forecast model: transformer                     | seconds to fit one seed   |                       |                   107.8    | single CPU core, no GPU                  |
