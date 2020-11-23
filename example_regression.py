# -*- encoding: utf-8 -*-
"""
==========
Regression
==========

The following example shows how to fit a simple regression model with
*auto-sklearn*.
"""
import sklearn.datasets
import sklearn.metrics

import autosklearn.regression


############################################################################
# Data Loading
# ============

X, y = sklearn.datasets.load_boston(return_X_y=True)

X_train, X_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, random_state=1)

############################################################################
# Build and fit a regressor
# =========================

automl = autosklearn.regression.AutoSklearnRegressor(
    # time_left_for_this_task=120,
    # per_run_time_limit=30,
    # tmp_folder='./tmp/tmp',
    # output_folder='./out/out',
    n_jobs=-1,
    delete_output_folder_after_terminate=False
)
automl.fit(X_train, y_train, dataset_name='boston')

automl.fit_ensemble(y_train, ensemble_size=50)

############################################################################
# Print the final ensemble constructed by auto-sklearn
# ====================================================

print(automl.show_models())

###########################################################################
# Get the Score of the final ensemble
# ===================================

predictions = automl.predict(X_test)
print("R2 score:", sklearn.metrics.r2_score(y_test, predictions))