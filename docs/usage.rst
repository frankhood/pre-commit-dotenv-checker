=====
Usage
=====

To use pre-commit dotenv checker in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pre_commit_dotenv_checker.apps.PreCommitHooksDjangoMigrationsConfig',
        ...
    )

Add pre-commit dotenv checker's URL patterns:

.. code-block:: python

    from pre_commit_dotenv_checker import urls as pre_commit_dotenv_checker_urls


    urlpatterns = [
        ...
        url(r'^', include(pre_commit_dotenv_checker_urls)),
        ...
    ]
