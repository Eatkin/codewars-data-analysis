// https://www.codewars.com/kata/5601409514fc93442500010b
// 2023-03-11T17:14:41.638+0000
const betterThanAverage = (classPoints, yourPoints) => classPoints.reduce((i, point) => i + point, 0) / classPoints.length < yourPoints;
