INSERT INTO animal_breed(name)
SELECT DISTINCT breed FROM animals;

INSERT INTO animal_type(name)
SELECT DISTINCT animal_type FROM animals;

INSERT INTO animal_color(name)
SELECT DISTINCT TRIM(color1) FROM animals
UNION
SELECT DISTINCT TRIM(color2) FROM animals;

INSERT INTO outcome_subtype(name)
SELECT DISTINCT outcome_subtype FROM animals;

INSERT INTO outcome_type(name)
SELECT DISTINCT outcome_type FROM animals;


INSERT INTO new_animals(age_upon_outcome,
                        animal_id,
                        name,
                        date_of_birth,
                        outcome_month,
                        outcome_year,
                        type_id,
                        breed_id,
                        color1_id,
                        color2_id,
                        outcome_subtype_id,
                        outcome_type_id
                        )
SELECT
    a.age_upon_outcome,
    a.animal_id,
    a.animals.name,
    a.date_of_birth,
    a.outcome_month,
    a.outcome_year,
    atp.id as type_id,
    ab.id as breed_id,
    ac1.id as color1_id,
    ac2.id as color2_id,
    ost.id as outcome_subtype_id,
    ot.id as outcome_type_id


FROM animals a
LEFT JOIN animal_breed ab ON ab.name = a.breed
LEFT JOIN animal_type atp ON a.animal_type = atp.name
LEFT JOIN animal_color ac1 ON ac1.name = a.color1
LEFT JOIN animal_color ac2 ON ac2.name = a.color2
LEFT JOIN outcome_subtype ost ON ost.name = a.outcome_subtype
LEFT JOIN outcome_type ot ON ot.name = a.outcome_type
