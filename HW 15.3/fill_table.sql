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
    (age_upon_outcome,
    animal_id,
    animals.name,
    date_of_birth,
    outcome_month,
    outcome_year,
    animal_type.id as type_id,
    animal_breed.id as breed_id,
    animal.color1.id as color1_id,
    anima.color2.id as color2_id,
    outcome_subtype.id as outcome_subtype_id,
    outcome_type.id as outcome_type_id
    )

FROM animals
LEFT JOIN animal_breed ab ON ab.name = animals.breed
LEFT JOIN animal_type at ON animals.animal_type = at.name
LEFT JOIN animal_color ac as animal_color1 ON animal_color1.name = animals.color1
LEFT JOIN animal_color ac as animal_color2 ON animal_color2.name = animals.color2
LEFT JOIN outcome_subtype  ON outcome_subtype.name = animals.outcome_subtype
LEFT JOIN outcome_type  ON outcome_type.name = animals.outcome_type
