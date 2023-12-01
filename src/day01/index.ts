import run from "aocrunner";

const numberWords = {
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

const parseInput = (rawInput: string) => {
  return rawInput.split("\n");
};

type NumberPos = {
  pos: number;
  value: string;
};

function extractDigits(line: string): NumberPos[] {
  let numbers: NumberPos[] = new Array();
  for (let i = 0; i < line.length; i++) {
    let n = Number(line[i]);
    if (!Number.isNaN(n)) {
      numbers.push({
        pos: i,
        value: line[i],
      });
    }
  }
  return numbers;
}

function extractWords(line: string): NumberPos[] {
  let numbers: NumberPos[] = new Array();
  for (let k of Object.keys(numberWords)) {
    let re = new RegExp(k, "g");
    const matches = line.matchAll(re);
    for (const match of matches) {
      numbers.push({
        pos: <number>match.index,
        value: numberWords[match[0] as keyof typeof numberWords],
      });
    }
  }
  return numbers;
}

function concatFirstLast(numbers: NumberPos[]): number {
  let sortedNumbers = numbers.sort((a, b) => (a.pos < b.pos ? -1 : 1));
  const l: number = sortedNumbers.length;
  return Number(sortedNumbers[0].value + sortedNumbers[l - 1].value);
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);

  let total = 0;
  for (let line of input) {
    let numbers = extractDigits(line);
    let s = concatFirstLast(numbers);
    total += s;
  }
  return total;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let total = 0;
  for (let line of input) {
    let numbers = extractDigits(line);
    numbers.push(...extractWords(line));
    let s = concatFirstLast(numbers);
    total += s;
  }
  return total;
};

run({
  part1: {
    tests: [
      {
        input: `
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        `,
        expected: 142,
      },
    ],
    solution: part1,
  },
  part2: {
    tests: [
      {
        input: `
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        `,
        expected: 281,
      },
    ],
    solution: part2,
  },
  trimTestInputs: true,
  // onlyTests: true,
});
