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

function extractDigits(line: string): string[] {
  let parts: string[] = [];
  for (let c of line) {
    let n = Number(c);
    if (!Number.isNaN(n)) {
      parts.push(c);
    }
  }
  return parts;
}

function replaceWords(line: string): string {
  for (let k in numberWords) {
    var re = new RegExp(k, "g");
    var l = k.length;
    var replace = k[0] + numberWords[k as keyof typeof numberWords] + k[l - 1];
    line = line.replace(re, replace);
  }
  return line;
}

function concatFirstLast(parts: string[]): number {
  const l: number = parts.length;
  return Number(parts[0] + parts[l - 1]);
}

const part1 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let total = 0;
  for (let line of input) {
    let parts = extractDigits(line);
    let s = concatFirstLast(parts);
    total += s;
  }
  return total;
};

const part2 = (rawInput: string) => {
  const input = parseInput(rawInput);
  let total = 0;
  for (let line of input) {
    line = replaceWords(line);
    let parts = extractDigits(line);
    let s = concatFirstLast(parts);
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
