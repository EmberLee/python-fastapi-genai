# About uv
Python 프로젝트와 패키지를 쉽고 빠르게 관리해주는 툴
- 공식 사이트: https://docs.astral.sh/uv/ 
- 참조: [uv : 엄청 빠르고 편리한 Python 프로젝트, 패키지 관리 프로그램](https://wiki.mattabu.com/blog/uv-fast-and-convenient-python-project-package-manager)

## 서론 - Python 패키징이 복잡해진 역사
![image](https://preview.redd.it/2o8wlapqk5h31.png?width=320&crop=smart&auto=webp&s=c86e1d224f0403adaafe5204b00bbb08a4edb946)

### 1. 초창기: easy_install
- 2000년대 후반~2010년대 초반에는 **PyPI**와 **pip** 가 지금처럼 성숙하지 않았습니다.
- 당시에는 **easy_install** 이 사실상 유일한 선택지였고, 설치한 패키지를 제거하거나, 설치된 패키지 버전을 지정·고정하는 기능이 부족해 많은 불편이 있었습니다.

### 2. pip의 등장
- **pip**는 requirements.txt를 통해 의존성을 고정하고 설치할 수 있는 기능을 제공하면서, 그야말로 Python 커뮤니티의 표준이 되었습니다.
- Python 공식 배포판에도 점차 포함되어 사실상 “파이썬 하면 pip”라는 인식이 굳어지기도 했습니다.

### 3. conda의 등장과 머신러닝 생태계
- **conda**는 주로 **NumPy, SciPy** 같은 과학 컴퓨팅 라이브러리를 쉽게 설치하고자 하는 목적에서 개발되었습니다.
- 하지만 **conda** 는 별도의 패키지 저장소(Anaconda Cloud, conda-forge)를 사용하고, pip 와는 분리된 자체 의존성 해석 방식, 가상환경 관리 방식을 채택하고 있어서 **생태계가 이원화**되는 문제를 야기했습니다.
- 그 결과, 리서쳐와 서비스 개발자 간의 소통 문제가 빈번히 발생해 왔습니다.

### 4. poetry의 부상
- **poetry**는 ``pyproject.toml``과 ``poetry.lock`` 기반으로 **의존성을 엄격히 고정**하고, 여러 플랫폼에서 재현 가능한 빌드를 제공한다는 점에서 각광을 받았습니다.
- 단점으로는, 복잡한 의존성을 가진 프로젝트에서 **해석 속도가 느리다**는 점이 종종 지적되었습니다.
- 그럼에도 **Poetry**는 **“제대로 동작하는 것을 보장한다”** 는 확실한 장점을 가진 덕분에, 비교적 규모가 큰 팀이나 오픈소스 프로젝트에서 널리 채택되었습니다.
- **pyenv, pipx, pipenv, pip-tools** 등의 도구도 각자 가상환경·의존성 관리, Python 버전 관리, 종속성 락(lock) 파일 관리 등 다양한 문제를 해결하고자 시도했습니다.
- 하지만 이런 도구마다 관점이 달라서, **서로 비슷한 기능이 겹치거나, 설정 방식이 달라** 숙련된 개발자조차 혼란스러워하는 지점이 많았습니다.

## uv의 주요 특징 및 장점
- **⚡️ 압도적인 속도**: `pip`보다 10~100배 더 빠릅니다.
- **🚀 통합된 도구**: `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv` 등의 여러 도구를 하나의 `uv`로 대체할 수 있습니다.
- **🏢 Cargo 스타일의 작업 공간 지원**: 대규모 프로젝트에서 확장 가능한 프로젝트 관리를 용이하게 합니다.
- **💾 디스크 공간 효율성**: 전역 캐시를 사용하여 종속성을 중복 제거합니다.
- **⏬ 간편한 설치**: Rust나 Python 설치 없이 `curl` 또는 `pip`를 통해 설치할 수 있습니다.
- **🖥️ 다양한 플랫폼 지원**: macOS, Linux, Windows를 지원합니다.
- **🔩 기존 워크플로우와의 호환성**: 기존 `pip`, `pip-tools`, `virtualenv` 명령어를 대체하여 사용할 수 있어 마이그레이션이 용이합니다.
- **🔗 표준 준수**: PEP 517, PEP 518, PEP 508, PEP 660 등 Python 표준을 완벽하게 지원합니다.
- **🐍 가상 환경 관리**: `uv venv` 명령어를 통해 Python 버전을 지정하여 가상 환경을 생성하고 관리할 수 있습니다.
- **✨ Python 버전 관리**: `uv python install` 명령어를 통해 필요한 Python 버전을 쉽게 설치하고 관리할 수 있습니다.
- **🎨 종속성 관리**: `uv add`, `uv remove` 명령어를 사용하여 패키지를 추가하고 제거하며, 개발용 종속성 및 extra 종속성 관리도 지원합니다.
- **🗂️ lock 파일 및 requirements.txt 지원**: `uv export -o requirements.txt` 명령어를 통해 `requirements.txt` 파일을 생성하고, `uv.lock` 파일을 통해 재현 가능한 빌드를 보장합니다.
- **❇️ 스크립트 실행**: `uv run` 명령어를 통해 가상 환경을 활성화하지 않고도 Python 스크립트를 실행할 수 있습니다.
- **🛠️ 도구 실행**: `uv tool run` (또는 `uvx`) 명령어를 통해 Python 패키지에서 제공하는 명령줄 도구를 실행할 수 있습니다.

## uv 설치
`pip install uv`로 설치할 수는 있지만, uv는 프로젝트 관리 툴이기에 특정 환경에 구애받게 설치되는 것보다는 아래의 방법을 이용해서 전역으로 설치하는 것을 추천합니다.

#### 윈도우
> ``` $ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" ```

#### Mac/Linux/WSL
> ``` $ curl -LsSf https://astral.sh/uv/install.sh | sh ```

## uv로 프로젝트 생성
> ``` $ uv init emberground ```

`emberground` 폴더 안에는 다음과 같은 파일들이 만들어집니다.
- `.gitignore` : git으로 관리하지 않을 파일을 지정합니다.
- `.python-version` : 이 프로젝트에서 사용할 파이썬의 버전이 명시&고정되어 있습니다. 디폴트는 가장 최신 버전. 필요하다면 다른 버전으로 바꾸어도 됩니다.
- `main.py` : 간단한 예제 프로그램이 들어 있습니다. 실질적으로 여기에 작업을 합니다.
- `pyproject.toml` : node.js 에 빗대면, package.json 에 해당이 됩니다. 필요한 파이썬 버전이 명시되어 있고, **의존성 및 메타데이터**를 정의하는 **핵심** 파일입니다.
- `README.md` : 이 프로젝트에 대한 설명을 적는 공간입니다.

## 프로젝트 실행
`emberground` 폴더로 들어가서 `uv run main.py` 를 실행합니다.
```
C:\work\emberground> uv run .\main.py
Using CPython 3.13.3
Creating virtual environment at: .venv
Hello from emberground!
C:\work\emberground>
```