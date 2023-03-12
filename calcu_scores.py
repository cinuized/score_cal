import random
import sys


class Score:
  max_score = 98
  min_score = 90
  n = 1
  average = 0
  numarr = [0]

  def __init__(self):
    
    self.n = int(sys.argv[1])
    self.average = int(sys.argv[2])

  def prepare_numbers(self):
    self.numarr = [random.randint(self.min_score, self.max_score)]
    # print(self.numarr)
    for numbers in range(0, self.n - 1):
      self.numarr = self.numarr + [random.randint(self.min_score, self.max_score)]
    
    # print(self.numarr)
    return self.numarr

  def generate_once(self):
    #TODO: generate scores.
    # self.numarr = self.prepare_numbers()
    # average = sum(self.numarr) / len(self.numarr)
    # print("%d" % int(average))
    # print(self.numarr)
    # print("Generated!")
    self.prepare_numbers()
    while (1):
      if (int(sum(self.numarr)/len(self.numarr)) == self.average):
        self.save_to_file()
        return self.numarr
      else:
        self.prepare_numbers()
        continue
      
  def save_to_file(self):
    f = open('score.txt', 'a')
    f.writelines(str(self.numarr)[1:-1] + "\n")
    f.close()


def main():
  score = Score()
  # print(score.average)
  # print(score.generate_once())
  # print(sum(score.numarr) / len(score.numarr))
  for n in range(0, int(sys.argv[3])):
    print(score.generate_once())

if __name__ == '__main__':
  main()