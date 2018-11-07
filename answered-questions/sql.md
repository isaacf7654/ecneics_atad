# Useful SQL code snippets

**Q**: How can I share my tables with (read privileges) specific people?

**A**:
```sql
grant select on all tables in schema aprivett to cfrankel, whaight;
grant usage on schema aprivett to cfrankel, whaight;
```

Note that you can replace users with a group, e.g.,
 `data_wranglers`.
