import pickle
pickle_file = open('my_pickled_list.pkl','rb')
recovered_list = pickle.load(pickle_file)
pickle_file.close()

print(recovered_list)
