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


### PostgreSQL Server Information
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

#### PostgreSQL Server Additional Information

<div class="termy">

```console
❯ pgperf server additional --help
                                                                               
 Usage: pgperf server additional [OPTIONS] COMMAND [ARGS]...                   
                                                                               
 Additional Supplied Modules                                                   
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ add-all-recommended-extensions  Adding Extensions [sslinfo, pg_buffercache, │
│                                 pg_stat_statements] to your database.       │
│ extensions                      Get available and installed extensions      │
╰─────────────────────────────────────────────────────────────────────────────╯
``` 
</div>

#### PostgreSQL Server Configuration 

<div class="termy">

```console
❯ pgperf server configuration --help
                                                                               
 Usage: pgperf server configuration [OPTIONS] COMMAND [ARGS]...                
                                                                               
 Server configuration information                                              
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ authentication           Show Authentication configuration                  │
│ connection-settings      Show Connection Settings configuration             │
│ disk                     Show Kernel Resource Usage configuration           │
│ file-locations           Show File Locations configuration                  │
│ kernel                   Show Kernel configuration                          │
│ memory                   Show Memory configuration                          │
│ replication              Server Replication information                     │
│ show-all                 Show all Server configuration                      │
│ ssl                      Show Authentication configuration                  │
│ vacuum                   Show Cost-based Vacuum Delay configuration         │
│ writer                   Show Background Writer configuration               │
╰─────────────────────────────────────────────────────────────────────────────╯
``` 
</div>

### PostgreSQL Server Stats

<div class="termy">

```console
❯ pgperf server stats --help
                                                                               
 Usage: pgperf server stats [OPTIONS] COMMAND [ARGS]...                        
                                                                               
 The Statistics Collector. PostgreSQL's statistics collector is a subsystem    
 that supports collection and reporting of information about server activity.  
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ collected             Collected Statistics Views                            │
│ dinamic               Dynamic Statistics Views                              │
╰─────────────────────────────────────────────────────────────────────────────╯
``` 
</div>

### PostgreSQL Server Stats Collected

<div class="termy">

```console
❯ pgperf server stats collected --help
                                                                               
 Usage: pgperf server stats collected [OPTIONS] COMMAND [ARGS]...              
                                                                               
 Collected Statistics Views                                                    
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ all-indexes          One row for each index in the current database,        │
│                      showing statistics about accesses to that specific     │
│                      index. See pg_stat_all_indexes for details.            │
│                      (Compatible with PostgresSQL >= 11.0 )                 │
│ all-tables           One row for each table in the current database,        │
│                      showing statistics about accesses to that specific     │
│                      table.  See pg_stat_all_tables for details.            │
│                      (Compatible with PostgresSQL >= 11.0 )                 │
│ archiver             One row only, showing statistics about the WAL         │
│                      archiver process's activity.  See pg_stat_archiver for │
│                      details. ( Compatible with PostgresSQL >= 11.0 )       │
│ bgwriter             One row only, showing statistics about the background  │
│                      writer process's activity.  See pg_stat_bgwriter for   │
│                      details. ( Compatible with PostgresSQL >= 11.0 )       │
│ database             One row per database, showing database-wide            │
│                      statistics.  See pg_stat_database for details.         │
│                      (Compatible with PostgresSQL >= 11.0 )                 │
│ database-conflicts   One row per database, showing database-wide statistics │
│                      about query cancels due to conflict with recovery on   │
│                      standby servers.  See pg_stat_database_conflicts for   │
│                      details. (Compatible with PostgresSQL >= 11.0 )        │
│ io-all-indexes       One row for each index in the current database,        │
│                      showing statistics  about I/O on that specific index.  │
│                      See pg_statio_all_indexes for details. (Compatible     │
│                      with PostgresSQL >= 11.0 )                             │
│ io-all-sequences     One row for each sequence in the current database,     │
│                      showing statistics about I/O on that specific          │
│                      sequence. See pg_statio_all_sequences  for details.    │
│                      (Compatible with PostgresSQL >= 11.0 )                 │
│ io-all-tables        One row for each table in the current database,        │
│                      showing statistics about I/O on that specific table.   │
│                      See pg_statio_all_tables for details. (Compatible with │
│                      PostgresSQL >= 11.0 )                                  │
│ io-sys-indexes       Same as pg_statio_all_indexes, except that only        │
│                      indexes on system tables are shown. (Compatible with   │
│                      PostgresSQL >= 11.0 )                                  │
│ io-sys-sequences     Same as pg_statio_all_sequences, except that only      │
│                      system sequences  are shown. (Presently, no system     │
│                      sequences are defined, so this view is always empty.)  │
│                      (Compatible with PostgresSQL >= 11.0 )                 │
│ io-sys-tables        Same as pg_statio_all_tables, except that only system  │
│                      tables are shown. (Compatible with PostgresSQL >= 11.0 │
│                      )                                                      │
│ io-user-indexes      Same as pg_statio_all_indexes, except that only        │
│                      indexes on user  tables are shown. (Compatible with    │
│                      PostgresSQL >= 11.0 )                                  │
│ io-user-sequences    Same as pg_statio_all_sequences, except that only user │
│                      sequences  are shown. (Compatible with PostgresSQL >=  │
│                      11.0 )                                                 │
│ io-user-tables       Same as pg_statio_all_tables, except that only user    │
│                      tables are shown. (Compatible with PostgresSQL >= 11.0 │
│                      )                                                      │
│ sys-indexes          Same as pg_stat_all_indexes, except that only indexes  │
│                      on system tables are shown. (Compatible with           │
│                      PostgresSQL >= 11.0 )                                  │
│ user-functions       One row for each tracked function, showing statistics  │
│                      about executions of that function. See                 │
│                      pg_stat_user_functions for details. (Compatible with   │
│                      PostgresSQL >= 11.0 )                                  │
│ user-tables          Same as pg_stat_all_tables, except that only user      │
│                      tables are shown. (Compatible with PostgresSQL >= 11.0 │
│                      )                                                      │
│ xact-all-tables      Similar to pg_stat_all_tables, but counts actions      │
│                      taken so far within  the current transaction (which    │
│                      are not yet included in pg_stat_all_tables and related │
│                      views). The columns for numbers of live and dead rows  │
│                      and vacuum and analyze actions are not present in this │
│                      view. (Compatible with PostgresSQL >= 11.0 )           │
│ xact-user-functions  Similar to pg_stat_user_functions, but counts only     │
│                      calls during the current transaction (which are not    │
│                      yet included in  pg_stat_user_functions). (Compatible  │
│                      with PostgresSQL >= 11.0 )                             │
│ xact-user-tables     Same as pg_stat_xact_all_tables, except that only user │
│                      tables are shown. (Compatible with PostgresSQL >= 11.0 │
│                      )                                                      │
╰─────────────────────────────────────────────────────────────────────────────╯

``` 
</div>

### PostgreSQL Server Stats Dinamic

<div class="termy">

```console
❯ pgperf server stats dinamic --help
                                                                               
 Usage: pgperf server stats dinamic [OPTIONS] COMMAND [ARGS]...                
                                                                               
 Dynamic Statistics Views                                                      
                                                                               
╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --verbose    --no-verbose          [default: no-verbose]                    │
│ --debug      --no-debug            [default: no-debug]                      │
│ --conf                       TEXT                                           │
│ --help                             Show this message and exit.              │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ activity          One row per server process, showing information related   │
│                   to the current  activity of that process, such as state   │
│                   and current query.  See pg_stat_activity for details. (   │
│                   >= PostgresSQL  11.0 )                                    │
│ progress-vacuum   One row for each backend (including autovacuum worker     │
│                   processes)  running VACUUM, showing current progress. (   │
│                   >= PostgresSQL  11.0 )                                    │
│ replication       One row per WAL sender process, showing statistics about  │
│                   replication  to that sender's connected standby server.   │
│                   See pg_stat_replication for details. ( >= PostgresSQL     │
│                   11.0 )                                                    │
│ ssl               One row per connection (regular and replication), showing │
│                   information  about SSL used on this connection. ( >=      │
│                   PostgresSQL  11.0 ) See pg_stat_ssl for details.          │
│ statements-reset  pg_stat_statements_reset discards statistics gathered so  │
│                   far by  pg_stat_statements ( >= PostgresSQL  11.0 )       │
│ subscription      At least one row per subscription, showing information    │
│                   about the  subscription workers.  See                     │
│                   pg_stat_subscription for details. ( >= PostgresSQL  11.0  │
│                   )                                                         │
│ wal-receiver      Only one row, showing statistics about the WAL receiver   │
│                   from that  receiver's connected server. See               │
│                   pg_stat_wal_receiver for details. ( >= PostgresSQL  11.0  │
│                   )                                                         │
╰─────────────────────────────────────────────────────────────────────────────╯

```
</div>

### PostgreSQL Table Information
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

### PostgreSQL Index Information
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