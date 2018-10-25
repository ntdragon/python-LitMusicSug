-- suggestions_schema.sql

-- Schema for both Psalm and Songs suggestions

create table sugg (
          id        integer primary key autoincrement not null,
          ly_yr     char(1) check("lit_yr" in ('A'.'B','C')),
          event     text,
          title     text,
          origin    text,
          idate     date
          unique(lit_year, event, suggestion, origin)
);