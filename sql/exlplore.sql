select count(*)
    from mimiciv_hosp.admissions;


SELECT subject_id, hadm_id, stay_id
FROM mimiciv_icu.icustays
LIMIT 10
