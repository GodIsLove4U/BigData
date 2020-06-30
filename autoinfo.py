from mrjob.job import MRJob
class Veh_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "Vehicle":
               yield "Vehicle", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Veh_count.run()