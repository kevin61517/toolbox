from flask_sqlalchemy import SQLAlchemy


class IsolationChangedSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options.update({'isolation_level': 'READ COMMITTED', })
        super(IsolationChangedSQLAlchemy, self).apply_driver_hacks(app, info, options)
