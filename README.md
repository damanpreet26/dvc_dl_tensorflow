# DVC - DL - TF - AIOPS  DEMO

## Commands

### Step 01: create a new environment
```bash
conda create -n new_env python=3.8 -y
```

### Step 02:  activate the new_env
```bash
conda activate new_env
```

### Step 03: initialize DVC
```bash
git init
dvc init
```

### Step 04: Create empty files
```bash
mkdir -p src src/utils cofig
touch dvc.yaml config/config.yaml params.yaml src/stage_01_load_save.py requirements.txt src/__init__.py src/utils/__init__.py
 ```

### Step 05: First commit



