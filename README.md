# Tracker/Changelog Exercise

This is an example django application that has sample models (in the `samples` app) and a `changelog` app that is used to track model instance changes.

## Configuration/Usage

This project assumes you'll be using a virtual environment and can `pip install -r requirements.txt` to setup the necessary requirements.

To add models for tracking changes, add the model labels to the `TRACKED_MODELS` list/tuple in the `settings.py` file.

For example, to track the `Organization` model in the `samples` app, you need an entry of `"samples.Organization"`. This example project already has both the `samples.Organization` and `samples.User` models in this setting.

Warning, do *not* add `"changelog.ChangeLog"` to this list or a race condition will likely occur.

### Tracked Changes

* created records
* updated records (*note:* see limitations section)
* deleted records (including bulk deletes)

### Limitations

This example has a significant number of limitations:
* bulk updated records (example: `MyModel.filter(a_field='something').update(a_field='something else')`) will not be tracked due to the Django ORM not sending signals for pre or post save on those records (i.e. the action is taken directly on the database)
* primary keys are currently assumed to always be integers. A future version could address this multiple ways depending on the change logs storage method (i.e. if another persistance layer was used). This ties back to handling of linking back to specific changes on specific models.
* many-to-many changes are not specifically handled in any special way. This could be addressed by expanding to use the many-to-many signal handling but again, more questions would need to be answered.
* non-JSON-serializable fields are currently not handled. This simplistic system does not attempt to develop standard serialization for database date/time fields or any other fields that are not directly JSON serializable.
* there are certainly more limitations that I've not thought of yet.

## Running Tests

The normal `./manage.py test` will work fine and includes a functional test which roughly matches the example given in the exercise.
