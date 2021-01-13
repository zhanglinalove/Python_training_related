-- #### 3. 为以下 sql 语句标注执行顺序: ####

-- 复制代码
-- SELECT DISTINCT player_id, player_name, count(*) as num 
-- FROM player JOIN team ON player.team_id = team.team_id 
-- WHERE height > 1.80 
-- GROUP BY player.team_id 
-- HAVING num > 2 
-- ORDER BY num DESC 
-- LIMIT 2


SELECT DISTINCT player_id, player_name, count(*) as num  # 5
FROM player JOIN team ON player.team_id = team.team_id   # 1
WHERE height > 1.80                                      # 2
GROUP BY player.team_id                                  # 3
HAVING num > 2                                           # 4
ORDER BY num DESC                                        # 6
LIMIT 2                                                  # 7

