import os
import shutil

server_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

if os.path.exists(server_path) and os.path.isdir(server_path):
    for app in os.listdir(server_path):
        if os.path.isdir(os.path.join(server_path, app)):
            migrations_path = os.path.join(server_path, app, 'migrations')
            if os.path.exists(migrations_path):
                migrations = os.listdir(migrations_path)
                if len(migrations) > 1:
                    for migration in migrations:
                        if migration != '__init__.py':
                            migration_path = os.path.join(
                                migrations_path, migration)
                            if os.path.isfile(migration_path):
                                os.remove(migration_path)
                                print(f'Deleted migration file: {migration_path}')
                            elif os.path.isdir(migration_path):
                                shutil.rmtree(migration_path)
                                print(f'Deleted migration directory: {migration_path}')
                    print(f'Deleted migrations for {app}')
                else:
                    print(f'Only __init__.py found in migrations for {app}')
            else:
                print(f'No migrations for {app}')

            pycache_path = os.path.join(server_path, app, '__pycache__')
            if os.path.exists(pycache_path) and os.path.isdir(pycache_path):
                shutil.rmtree(pycache_path)
                print(f'Deleted __pycache__ for {app}')
else:
    print('Server directory does not exist')