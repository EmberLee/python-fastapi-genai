# python-fastapi-genai
Studying basic concept of FastAPI &amp; uv

- [python-fastapi-genai](#python-fastapi-genai)
- [How to Start](#how-to-start)
  - [Linux 실행환경 구성](#linux-실행환경-구성)
  - [샘플 코드 실행하기](#샘플-코드-실행하기)
    - [Parameters](#parameters)
  - [모듈 코어 함수 실행하기](#모듈-코어-함수-실행하기)
- [함수 I/F 상세 설명](#함수-if-상세-설명)
  - [Developer Ground Rule](#developer-ground-rule)
    - [소스 외부 (Parsing Rule)](#소스-외부-parsing-rule)
    - [소스 내부 (Logging Level Rule)](#소스-내부-logging-level-rule)
      - [ERROR](#error)
      - [DEBUG](#debug)
      - [INFO](#info)
  - [Contribution](#contribution)

# How to Start

처음으로 해야 할 일은 `uv`를 설치하는 것입니다.
`uv`에 대해서는 [<u> uv 가이드</u>](./Guide_uv.md)에서 더 자세히 확인하실 수 있습니다.

## Linux 실행환경 구성
```bash
bash resources/setup.sh
```
스크립트 실행 후 `LibSSL Downgraded. ==> 1.0.0` 이라는 메시지가 출력되면 실행환경 구성이 완료됩니다.

## 샘플 코드 실행하기
샘플 코드를 사용하여 특정 폴더의 ppt, pptx 파일을 전처리해볼 수 있습니다.
```bash
python main_prep.py debug -tdir=ppt_samples/ -sdir=ppt_results/ -format=ppt,pptx -vt=unix
```

### Parameters
|옵션|타입|설명|default|
|---|---|---|---|
|{}|str|log level & .ini 파일 로드 분기 결정 파라미터||
|--target_dir, -tdir|str|txt 변환 대상인 원천 파일 경로, 대상 파일명이 포함되어도 무방함.|./|
|--save_dir, -sdir|str|txt 변환 후 저장 경로 (plain/unix/latex 등 전처리 방식에 따라 하위 디렉토리 추가 생성됨)|results|
|--view_type, -vt|str|표 전처리 방식 지정 (plain/unix/html/md/latex) -> 전처리 설계서 참조|unix|

## 모듈 코어 함수 실행하기
함수로 제공되는 ppt 전처리 모듈은 PreproPpt 함수명으로 제공하고 있으며, 이 함수는 전달받은 파라미터에 따라 PPTX 파일을 분석하고, 각 페이지 단위로 TEXT 파일을 생성하는 Python 함수입니다.

```sh
from prepro_ppt import PreproPpt
 
infos, error_file_list, error_slide_dict = PreproPpt(filepath='ppt_samples/',
                                                     table_prepro='unix',
                                                     fileformat=('ppt', 'pptx'),
                                                     page_num=-1,
                                                     save_dir='results/240103/',
                                                     save_per_slide=True,
                                                     debugging_mode=False)
```

# 함수 I/F 상세 설명

## Developer Ground Rule

### 소스 외부 (Parsing Rule)
- 모든 shape 객체 사이에는 "\n\n" 구분자가 append 되어, 파싱 단위가 분간됨.
- 클러스터링, 권역, 제목&소제목 파싱 후에도 마찬가지로 "\n\n" 구분자가 따라붙어 결과적으로 상기한 특정 로직 수행 후에는 "\n\n\n" 구분자 파싱 후 다음 shape 객체가 파싱됨.
```
OLED 설계 변경
불량 개선을 위해, 보호 막 형성 (XX 모델 참조)
 1안. 막 형성 1차 시도 – 영역 구성 및 layer 판별
 2안. 두 번째 막 점검 이후 부터 막들뜸 현상 확인 및 신뢰성 문제 반영

기존
증착 영역 layer 기준 유기막 판정 불량
So Cute Dog
Glaring something
기존 내용 1
기존 내용 2


1안
막들뜸 불량을 개선하기 위한 조치 방안 1
Sad Dog…
1안 내용 1
1안 내용 2
```

### 소스 내부 (Logging Level Rule)

#### ERROR
- slide 전처리에 문제가 생기는 경우 (내부에서 Raise 하는 경우)

> ``` LOGGER.error(f"[PREPRO]\n{내용}") ```
```bash
ex) xxx.pptx 파일 전체 전처리에 실패했습니다.
ex) xxx.pptx 파일 Slide_x 전처리에 실패했습니다.
```

#### DEBUG
- 기존 디버그 모드에서 출력하는 요소들과 같이 객체 정보 파악을 위해 필요한 정보 출력
	- 동일 정보들이 중복해서 출력되지 않고 한번만 출력될 수 있도록 필요없는것들은 지우기
	
> ``` LOGGER.debug(f"[PREPRO]\n{내용}") ```

#### INFO
- 전처리 결과에 대한 summary 출력

> ``` LOGGER.info(f"[PREPRO]\n{내용}") ```

## Contribution
- 이잉걸: ingulbull@gmail.com&emsp;&nbsp;|  [AI Engineer]