# 2017/07/11
# viterbi algorithm
# reference: Wikipedia(en) https://en.wikipedia.org/wiki/Viterbi_algorithm

obs = ('normal', 'cold', 'dizzy')
states = ('healthy', 'fever')
start_path = {'healthy': 0.6, 'fever': 0.4}
trans_path = {
	'healthy': {'healthy': 0.7, 'fever': 0.3},
	'fever': {'healthy': 0.4, 'fever': 0.6}
}
emit_path = {
	'healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
	'fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
}

def viterbi(obs, states, start_path, trans_path, emit_path):
	v = [{}]
	for st in states:
		v[0][st] = {"prob": start_path[st] * emit_path[st][obs[0]], "prev": None}

	# run viterbi when t > 0
	for t in range(1, len(obs)):
		v.append({})
		for st in states:
			max_trans_p = max(v[t-1][prev_st]["prob"]*trans_path[prev_st][st] for prev_st in states)
			for prev_st in states:
				if v[t-1][prev_st]["prob"] * trans_path[prev_st][st] == max_trans_p:
					max_prob = max_trans_p * emit_path[st][obs[t]]
					v[t][st] = {"prob": max_prob, "prev": prev_st}
					break

	for line in dptable(v):
			print line

	opt = []

	# The highest probability
	max_prob = max(value["prob"] for value in v[-1].values())
	previous = None

	# Get most probable state and its backtrack
	for st, data in v[-1].items():
		if data["prob"] == max_prob:
			opt.append(st)
			previous = st
			break

	# Follow the backtrack till the first observation
	for t in range(len(v) - 2, -1, -1):
		opt.insert(0, v[t + 1][previous]["prev"])
		previous = v[t + 1][previous]["prev"]

	print 'The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob

def dptable(v):

    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(v)))
    for state in v[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v1[state]["prob"]) for v1 in v)

if __name__ == '__main__':
	viterbi(obs, states, start_path, trans_path, emit_path)	 



