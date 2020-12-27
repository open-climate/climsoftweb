# Climsoft Web

[![Build Status](https://travis-ci.org/climsoft/climsoftweb.svg?branch=master)](https://travis-ci.org/climsoft/climsoftweb)
[![codecov](https://codecov.io/gh/climsoft/climsoftweb/branch/master/graph/badge.svg)](https://codecov.io/gh/climsoft/climsoftweb)

Web application for secure data entry into Climsoft database.

---

## Roadmap

|      | Version | Designation | Database    | Server-side  | ORM        | Client-side           |
|------|---------|-------------|-------------|--------------|------------|-----------------------|
| 2020 |  0.x    | Prototype   | PostgreQL   | Django       | Django ORM | Bootstrap 4           |
| 2021 |  1.x    | Production  | MySQL       | Flask        | SQLAlchemy | Bootstrap 4           |
| 2022 |  2.x    | Optimized   | PostgreSQL+ | Flask        | SQLAlchemy | Preact Web Components |

Notes:
- Version 1.0+ building on ClimsoftWeb prototype
  - This version switches to Flask and SQLAlchemy to add support for tables with composite primary keys.
  - The default database returns to MySQL/MariaDB to allow a single server to host the CDMS and application databases
- Version 2.0+ will use the OpenCDMS architecture
  - This sees a return to PostgreSQL for the application database in anticipation that multiple database servers will be supported and are likely to be on different hardware
  - The client-side will switch to using Web Components (possibly using preact). See discussiond of Bootstrap 5 [dropping jQuery](https://www.infoq.com/news/2020/08/bootsrap-5-drops-jquery/) and Internet Explorer support
