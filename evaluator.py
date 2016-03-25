
import empirical

# Connect to Solver
solver = empirical.Solver()

# Send problems to solvers
dataset = [(1,2), (3,4), (2,-3)]
solutions = []
for problem in dataset:
    solutions.append(solver.solve(*problem))

# Evaluate solutions against ground truth
answers = [3, 7, -1]
correct_count = 0
for i in xrange(len(dataset)):
    if solutions[i] == answers[i]:
        correct_count = correct_count + 1

accuracy = correct_count / len(dataset)

# Save results
results = {
    'overall': {
        'type': 'table',
        'metric': 'Accuracy',
        'value': accuracy
    }
}
empirical.postResults(results)
