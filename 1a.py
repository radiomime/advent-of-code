from dataclasses import dataclass


@dataclass
class Elf:
    snacks: list[int]
    totalCalories: int


def getBlankElf() -> Elf:
    return Elf([], 0)


def getElves():
    elves = []
    elf = getBlankElf()

    with open("1a.input.txt") as f:
        for line in f:
            line = line.strip()
            if line != "":
                elf.snacks.append(int(line))
                elf.totalCalories = elf.totalCalories + int(line)
            else:
                elves.append(elf)
                elf = getBlankElf()

    return elves


def getWorstElf(elves):
    worstElf = getBlankElf()

    for elf in elves:
        if elf.totalCalories < worstElf.totalCalories:
            worstElf = elf

    return worstElf


def getBestElf(elves):
    bestElf = getBlankElf()

    for elf in elves:
        if elf.totalCalories > bestElf.totalCalories:
            bestElf = elf

    return bestElf


def sortElves(elves):
    return sorted(elves, key=lambda elf: elf.totalCalories)


def getBestXElfs(elves: list[Elf], x: int):
    return sortElves(elves)[-x:]


def combineElfFood(elves):
    total = 0
    for elf in elves:
        total = total + elf.totalCalories
    return total


if __name__ == "__main__":
    elves = getElves()

    # print(sortElves(elves))

    # bestElf = getBestElf(elves)
    # print(bestElf)
    bestElves = getBestXElfs(elves, 3)
    print(bestElves)
    print(combineElfFood(bestElves))
