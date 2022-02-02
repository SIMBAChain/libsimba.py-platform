from test_simba_hinted import TestSimbaHinted

tsh = TestSimbaHinted()
first = [[1,1,1,1]]
# tsh.nested_arr_2(first=first)
query_args = {}
qry_mth = True
res = tsh.nested_arr_2(first=first, query_args = {}, qry_mth = True)
print(res)