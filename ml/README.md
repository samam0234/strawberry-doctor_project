# ml

딸기 잎 질병 분류에 쓰는 학습 가중치입니다.

| 파일 | 설명 |
| --- | --- |
| `best_efficientnetb3_hard_finetune.pth` | EfficientNet-B3, 5클래스. 파일 크기는 약 41MB |

백엔드는 이 파일을 직접 탐색하지 않습니다. `back/.env`의 `ML_MODEL_PATH`가 가리키는 경로를 [`inference.py`](../back/diagnosis/services/README.md)가 로드합니다. Compose에서는 `./ml`이 컨테이너에 마운트되므로, 컨테이너 안에서 이 파일에 닿는 경로를 `ML_MODEL_PATH`에 적습니다.

가중치를 바꿀 때는 분류 헤드가 5개인지, 클래스 인덱스가 아래와 같은지 확인합니다.

| 인덱스 | 코드 |
| --- | --- |
| 0 | `wilt` |
| 1 | `phytophthora` |
| 2 | `tipburn` |
| 3 | `normal` |
| 4 | `yellowing` |

입력 크기는 300, 정규화는 ImageNet 평균과 표준편차입니다. 학습 코드는 이 디렉터리에 없고, 추론만 `back`에 있습니다.
