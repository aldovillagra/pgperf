# Python PostgreSQL Performance Tools

Python port of [Heroku PG Extras](https://github.com/heroku/heroku-pg-extras) with several additions and improvements. The goal of this project is to provide powerful insights into the PostgreSQL database for Python apps that are not using the Heroku PostgreSQL plugin.

Queries can be used to obtain information about a Postgres instance, that may be useful when analyzing performance issues. This includes information about locks, index usage, buffer cache hit ratios and vacuum statistics.

## Requirements

Python 3.8+

## Installation

<div class="termy">

```console
$ pip install pgperf
---> 100%
Successfully installed pgperf
```

</div>



Some of the queries (e.g., `calls` and `outliers`) require [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) extension enabled.

You can check if it is enabled in your database by running:

<div class="termy">

```console
pgperf server additional extensions
```
</div>

You should see the similar line in the output:

<div class="termy">

```console
| pg_stat_statements  | 1.7  | 1.7 | track execution statistics of all SQL statements executed |
```

</div>

## Usage

Please edit the config in your home directory, the file name is .pgperf.yml

```yaml
prod:
  db:
    server: 127.0.0.1
    port: 5432
    db: prod_db_name
    user: prod_db_user
    password: prod_db_pass
```

You can any commands, you can see all available command running:

<div class="termy">

```console
pgperf --help

Usage: pgperf [OPTIONS] COMMAND [ARGS]...                                                                                                                                                     
                                                                                                                                                                                               
 Python port of [Heroku PG Extras](https://github.com/heroku/heroku-pg-extras) with several additions and improvements.                                                                        
 The goal of this project is to provide powerful insights into the PostgreSQL database for Python apps that are not using the Heroku PostgreSQL plugin.                                        
                                                                                                                                                                                               
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --conf                      TEXT                                                                                                                                   │
│ --install-completion              Install completion for the current shell.                                                                                        │
│ --show-completion                 Show completion for the current shell, to copy it or customize the installation.                                                 │
│ --help                            Show this message and exit.                                                                                                      │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ all-locks                                    List all current locks in your database                                                                               │
│ blocking                                     Get all statements that are currently holding locks in your database                                                  │
│ buffercache-stats                            Get all Buffercache Stats                                                                                             │
│ buffercache-usage                            Get all Buffercache Usage                                                                                             │
│ cache-hits                                   Get all cache hits                                                                                                    │
│ calls                                        Get the queries that have highest frequency of execution                                                              │
│ calls-legacy                                 Get the queries that have highest frequency of execution                                                              │
│ index                                        Index Informations                                                                                                    │
│ locks                                        Queries with active exclusive locks                                                                                   │
│ long-running-queries                         All queries longer than five minutes by descending duration                                                           │
│ outliers                                     Queries that have longest execution time in aggregate                                                                 │
│ server                                       Server Informations                                                                                                   │
│ table                                        Table Informations                                                                                                    │
│ version                                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
</div>

