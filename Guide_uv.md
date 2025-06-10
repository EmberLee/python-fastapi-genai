# About uv
Python 프로젝트와 패키지를 쉽고 빠르게 관리해주는 툴
- 공식 사이트: https://docs.astral.sh/uv/ 
- 참조: [uv : 엄청 빠르고 편리한 Python 프로젝트, 패키지 관리 프로그램](https://wiki.mattabu.com/blog/uv-fast-and-convenient-python-project-package-manager)

## uv의 주요 특징 및 장점
- **압도적인 속도**: `pip`보다 10~100배 더 빠릅니다.
- **통합된 도구**: `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv` 등의 여러 도구를 하나의 `uv`로 대체할 수 있습니다.
- **Cargo 스타일의 작업 공간 지원**: 대규모 프로젝트에서 확장 가능한 프로젝트 관리를 용이하게 합니다.
- **디스크 공간 효율성**: 전역 캐시를 사용하여 종속성을 중복 제거합니다.
- **간편한 설치**: Rust나 Python 설치 없이 `curl` 또는 `pip`를 통해 설치할 수 있습니다.
- **다양한 플랫폼 지원**: macOS, Linux, Windows를 지원합니다.
- **기존 워크플로우와의 호환성**: 기존 `pip`, `pip-tools`, `virtualenv` 명령어를 대체하여 사용할 수 있어 마이그레이션이 용이합니다.
- **표준 준수**: PEP 517, PEP 518, PEP 508, PEP 660 등 Python 표준을 완벽하게 지원합니다.
- **가상 환경 관리**: `uv venv` 명령어를 통해 Python 버전을 지정하여 가상 환경을 생성하고 관리할 수 있습니다.
- **Python 버전 관리**: `uv python install` 명령어를 통해 필요한 Python 버전을 쉽게 설치하고 관리할 수 있습니다.
- **종속성 관리**: `uv add`, `uv remove` 명령어를 사용하여 패키지를 추가하고 제거하며, 개발용 종속성 및 extra 종속성 관리도 지원합니다.
- **lock 파일 및 requirements.txt 지원**: `uv export -o requirements.txt` 명령어를 통해 `requirements.txt` 파일을 생성하고, `uv.lock` 파일을 통해 재현 가능한 빌드를 보장합니다.
- **스크립트 실행**: `uv run` 명령어를 통해 가상 환경을 활성화하지 않고도 Python 스크립트를 실행할 수 있습니다.
- **도구 실행**: `uv tool run` (또는 `uvx`) 명령어를 통해 Python 패키지에서 제공하는 명령줄 도구를 실행할 수 있습니다.

## uv 설치

#### 윈도우
> ``` $ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" ```

#### Mac/Liuux
> ``` $ curl -LsSf https://astral.sh/uv/install.sh | sh ```

## uv로 프로젝트 생성
> ``` $ uv init emberground ```

`example` 폴더 안에는 다음과 같은 파일들이 만들어집니다.
- `.gitignore` : git으로 관리하지 않을 파일을 지정합니다.
- `.python-version` : 이 프로젝트에서 사용할 파이썬의 버전이 명시되어 있어요. 가장 최신 버전이 설정되어 있어요. 필요하다면 다른 버전으로 바꾸어도 됩니다.
- `main.py` : 간단한 예제 프로그램이 들어 있어요. 실질적으로 여기에 작업을 해야겠지요.
- `pyproject.toml` : **중요한 파일**입니다. node.js 로 보면, package.json 에 해당이 되요. 필요한 파이썬 버전이 명시되어 있고, 패키지에 대한 의존성 관리를 할 수 있어요.
- `README.md` : 이 프로젝트에 대한 설명을 적는 공간입니다.