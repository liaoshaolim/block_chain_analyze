# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Modelfromdict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ModelElement:
    tokenName: Optional[str] = None
    rank: Optional[int] = None
    lowestDate18_19: Optional[str] = None
    lowestPrice18_19: Optional[float] = None
    lowestDate18_20: Optional[str] = None
    lowestPrice18_20: Optional[float] = None
    usdtPrice: Optional[float] = None
    marketCap: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ModelElement':
        assert isinstance(obj, dict)
        tokenName = from_union([from_str, from_none], obj.get("tokenName"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        lowestDate18_19 = from_union(
            [from_str, from_none], obj.get("lowestDate_18_19"))
        lowestPrice18_19 = from_union(
            [from_float, from_none], obj.get("lowestPrice_18_19"))
        lowestDate18_20 = from_union(
            [from_str, from_none], obj.get("lowestDate_18_20"))
        lowestPrice18_20 = from_union(
            [from_float, from_none], obj.get("lowestPrice_18_20"))
        usdtPrice = from_union([from_float, from_none], obj.get("usdtPrice"))
        marketCap = from_union([from_float, from_none], obj.get("marketCap"))
        return ModelElement(tokenName, rank, lowestDate18_19, lowestPrice18_19, lowestDate18_20, lowestPrice18_20, usdtPrice, marketCap)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tokenName"] = from_union([from_str, from_none], self.tokenName)
        result["rank"] = from_union([from_int, from_none], self.rank)
        result["lowestDate_18_19"] = from_union(
            [from_str, from_none], self.lowestDate18_19)
        result["lowestPrice_18_19"] = from_union(
            [to_float, from_none], self.lowestPrice18_19)
        result["lowestDate_18_20"] = from_union(
            [from_str, from_none], self.lowestDate18_20)
        result["lowestPrice_18_20"] = from_union(
            [to_float, from_none], self.lowestPrice18_20)
        result["usdtPrice"] = from_union([to_float, from_none], self.usdtPrice)
        result["marketCap"] = from_union([to_float, from_none], self.marketCap)
        return result


def Modelfromdict(s: Any) -> List[ModelElement]:
    return from_list(ModelElement.from_dict, s)


def Modeltodict(x: List[ModelElement]) -> Any:
    return from_list(lambda x: to_class(ModelElement, x), x)
