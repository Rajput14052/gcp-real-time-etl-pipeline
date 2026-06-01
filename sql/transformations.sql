CREATE OR REPLACE TABLE `project.dataset.qualimetry_gold_metrics`
PARTITION BY DATE(processed_at)
CLUSTER BY project_key, status AS
SELECT
  project_key,
  status,
  COUNT(issue_id) AS total_issues,
  COUNTIF(status = 'Done') AS completed_issues,
  COUNTIF(status != 'Done') AS pending_issues,
  CURRENT_TIMESTAMP() AS processed_at
FROM `project.dataset.qualimetry_silver_issues`
GROUP BY project_key, status;
