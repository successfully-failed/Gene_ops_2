from Uber_object import Powerobject as Obj

obj = Obj()

obj.string = "GAGAGAGGAGAGAGAGAGGAGGGAGAG"
obj.opt_a = "1"
obj.opt_b = "1"
#obj.do_all_replication(
obj.do_all_translation()
print(obj.transl_out)
print("string",obj.string)
print("reformed",obj.reformed)
print("codons",obj.codons)
print("protein",obj.protein)
print("output", obj.transl_out)
