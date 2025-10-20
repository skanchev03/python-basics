pool_size = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
worker_absense = float(input())

pipe_one_liters = pipe_one_debit * worker_absense
pipe_two_liters = pipe_two_debit * worker_absense

total_liters = pipe_one_liters + pipe_two_liters

if total_liters <= pool_size:
    print(f'The pool is {total_liters * 100 / pool_size:.2f}% full.'
        f' Pipe 1: {pipe_one_liters * 100 / total_liters:.2f}%.'
        f' Pipe 2: {pipe_two_liters * 100 / total_liters:.2f}%.')
elif total_liters > pool_size:
    print(f'For {worker_absense:.2f}'
          f' hours the pool overflows with {total_liters - pool_size:.2f} liters.')
