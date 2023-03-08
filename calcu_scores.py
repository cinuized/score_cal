import random


class Score:
  max_score = 0
  min_score = 0
  n = 1
  average = 0

  def __init__(self, max_score, min_score, n, average):
    self.max_score = max_score
    self.min_score = min_score
    self.n = n
    self.average = average

  def prepare_numbers(self):
    numarr = [random.randint(60, 98)]
    print(numarr)
    for numbers in range(0, self.n - 1):
      numarr = numarr + [random.randint(60, 98)]
    
    print(numarr)
    return numarr

  def generate(self):
    #TODO: generate scores.
    numarr = self.prepare_numbers()
    print(sum(numarr) / len(numarr))
    print(numarr)
    print("Generated!")



def main():
  score = Score(60, 98, 7, 87)
  score.prepare_numbers()
  score.generate()

if __name__ == '__main__':
  main()