# docker-example

to use a container on dcc, put this the slurm file (.q file)

```slurm
#!/bin/bash
#
#SBATCH --job-name=bios823toyex
#SBATCH --mail-user=
#SBATCH --mail-type=END,FAIL
#SBATCH --mem=1024
#SBATCH --time=03:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=example-%J.stdout
#SBATCH --error=example-%J.stderr

mysif=dir-of-container/container.sif


singularity exec \
  ${mysif} \
  python run.py"
```
