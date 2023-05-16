-- https://www.codewars.com/kata/5ab828bcedbcfc65ea000099
-- 2023-05-03T14:30:28.925+0000
-- i choose you! --
SELECT pokemon.pokemon_name, pokemon.str * multipliers.multiplier AS modifiedStrength, multipliers.element
FROM pokemon
INNER JOIN multipliers ON pokemon.element_id = multipliers.id
WHERE modifiedStrength >= 40
ORDER BY modifiedStrength DESC;