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
❯ pgperf server additional extensions
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

You can run any commands, you can see all available command running:

<div class="termy">

```console
❯ pgperf --help
Usage: pgperf [OPTIONS] COMMAND [ARGS]...                                     
                                                                               
 Python port of [Heroku PG Extras](https://github.com/heroku/heroku-pg-extras) 
 with several additions and improvements.                                      
 The goal of this project is to provide powerful insights into the PostgreSQL  
 database for Python apps that are not using the Heroku PostgreSQL plugin.     
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --conf                      TEXT                                            │
│ --install-completion              Install completion for the current shell. │
│ --show-completion                 Show completion for the current shell, to │
│                                   copy it or customize the installation.    │
│ --help                            Show this message and exit.               │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ all-locks             List all current locks in your database               │
│ blocking              Get all statements that are currently holding locks   │
│                       in your database                                      │
│ buffercache-stats     Get all Buffercache Stats                             │
│ buffercache-usage     Get all Buffercache Usage                             │
│ cache-hits            Get all cache hits                                    │
│ calls                 Get the queries that have highest frequency of        │
│                       execution                                             │
│ calls-legacy          Get the queries that have highest frequency of        │
│                       execution                                             │
│ index                 Index Informations                                    │
│ locks                 Queries with active exclusive locks                   │
│ long-running-queries  All queries longer than five minutes by descending    │
│                       duration                                              │
│ outliers              Queries that have longest execution time in aggregate │
│ server                Server Informations                                   │
│ table                 Table Informations                                    │
│ version                                                                     │
╰─────────────────────────────────────────────────────────────────────────────╯

```
</div>


### Server
<div class="termy">

```console
❯ pgperf server --help
                                                                               
 Usage: pgperf server [OPTIONS] COMMAND [ARGS]...                              
                                                                               
 Server Informations                                                           
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ active-conections  List all active connections in this moments in your      │
│                    database                                                 │
│ additional         Additional Supplied Modules                              │
│ configuration      Server configuration information                         │
│ db-settings        Get the DB Settings                                      │
│ kill-all           Kill all the active database connections                 │
│ ssl-used           Check if SSL connection is used                          │
│ stats              The Statistics Collector. PostgreSQL's statistics        │
│                    collector is a subsystem that supports collection and    │
│                    reporting of information about server activity.          │
│ vacuum-stats       Dead rows and whether an automatic vacuum is expected to │
│                    be triggered                                             │
╰─────────────────────────────────────────────────────────────────────────────╯

``` 
</div>

### Table
<div class="termy">

```console
❯ pgperf table --help
                                                                               
 Usage: pgperf table [OPTIONS] COMMAND [ARGS]...                               
                                                                               
 Table Informations                                                            
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ bloat            Estimation of table 'bloat' space allocated to a relation  │
│                  that is full of dead tuples, that has yet to be reclaimed. │
│ cache-hit        Calculates your cache hit rate for reading tables          │
│ index-scans      Count of index scans by table descending by order          │
│ index-size       Total size of all the indexes on each table, descending by │
│                  size                                                       │
│ records-rank     All tables and the number of rows in each ordered by       │
│                  number of rows descending                                  │
│ seq-scans        Count of sequential scans by table descending by order     │
│ size             Size of the tables (excluding indexes), descending by size │
│ size-with-index  Size of the tables (including indexes), descending by size │
╰─────────────────────────────────────────────────────────────────────────────╯

``` 
</div>

### Index
<div class="termy">

```console
❯ pgperf index --help
                                                                               
 Usage: pgperf index [OPTIONS] COMMAND [ARGS]...                               
                                                                               
 Index Informations                                                            
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ all         List all the indexes with their corresponding tables and        │
│             columns.                                                        │
│ cache-hit   Calculates your cache hit rate for reading indexes              │
│ duplicate   Show multiple indexes that have the same set of columns, same   │
│             opclass, expression and predicate.                              │
│ null        Find indexes with a high ratio of NULL values                   │
│ scans       Number of scans performed on indexes                            │
│ size        The size of indexes, descending by size, in MB.                 │
│ total-size  Total size of all indexes in MB                                 │
│ unused      Unused and almost unused indexes. Ordered by their size         │
│             relative to the number of index scans. Exclude indexes of very  │
│             small tables (less than 5 pages), where the planner will almost │
│             invariably select a sequential scan, but may not in the future  │
│             as the table grows                                              │
│ usage       Index hit rate (effective databases are at 99% and up)          │
╰─────────────────────────────────────────────────────────────────────────────╯

``` 
</div>