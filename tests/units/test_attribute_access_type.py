from __future__ import annotations

from typing import Dict, List, Optional, Type, Union

import attrs
import pydantic.v1
import pytest
import sqlalchemy
import sqlmodel
from sqlalchemy import JSON, TypeDecorator
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

import reflex as rx
from reflex.utils.types import GenericType, get_attribute_access_type


class SQLAType(TypeDecorator):
    """SQLAlchemy custom dict type."""

    impl = JSON

    @property
    def python_type(self) -> Type[Dict[str, str]]:
        """Python type.

        Returns:
            Python Type of the column.
        """
        return Dict[str, str]


class SQLABase(DeclarativeBase):
    """Base class for bare SQLAlchemy models."""

    type_annotation_map = {
        # do not use lower case dict here!
        # https://github.com/sqlalchemy/sqlalchemy/issues/9902
        Dict[str, str]: SQLAType,
    }


class SQLATag(SQLABase):
    """Tag sqlalchemy model."""

    __tablename__: str = "tag"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


class SQLALabel(SQLABase):
    """Label sqlalchemy model."""

    __tablename__: str = "label"
    id: Mapped[int] = mapped_column(primary_key=True)
    test_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey("test.id"))
    test: Mapped[SQLAClass] = relationship(back_populates="labels")
    test_dataclass_id: Mapped[int] = mapped_column(
        sqlalchemy.ForeignKey("test_dataclass.id")
    )
    test_dataclass: Mapped[SQLAClassDataclass] = relationship(back_populates="labels")


class SQLAClass(SQLABase):
    """Test sqlalchemy model."""

    __tablename__: str = "test"
    id: Mapped[int] = mapped_column(primary_key=True)
    count: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
    int_list: Mapped[List[int]] = mapped_column(
        sqlalchemy.types.ARRAY(item_type=sqlalchemy.INTEGER)
    )
    str_list: Mapped[List[str]] = mapped_column(
        sqlalchemy.types.ARRAY(item_type=sqlalchemy.String)
    )
    optional_int: Mapped[Optional[int]] = mapped_column(nullable=True)
    sqla_tag_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey(SQLATag.id))
    sqla_tag: Mapped[Optional[SQLATag]] = relationship()
    labels: Mapped[List[SQLALabel]] = relationship(back_populates="test")
    # do not use lower case dict here!
    # https://github.com/sqlalchemy/sqlalchemy/issues/9902
    dict_str_str: Mapped[Dict[str, str]] = mapped_column()

    @property
    def str_property(self) -> str:
        """String property.

        Returns:
            Name attribute
        """
        return self.name

    @hybrid_property
    def str_or_int_property(self) -> Union[str, int]:
        """String or int property.

        Returns:
            Name attribute
        """
        return self.name

    @hybrid_property
    def first_label(self) -> Optional[SQLALabel]:
        """First label property.

        Returns:
            First label
        """
        return self.labels[0] if self.labels else None


class SQLAClassDataclass(MappedAsDataclass, SQLABase):
    """Test sqlalchemy model."""

    id: Mapped[int] = mapped_column(primary_key=True)
    no_default: Mapped[int] = mapped_column(nullable=True)
    count: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()
    int_list: Mapped[List[int]] = mapped_column(
        sqlalchemy.types.ARRAY(item_type=sqlalchemy.INTEGER)
    )
    str_list: Mapped[List[str]] = mapped_column(
        sqlalchemy.types.ARRAY(item_type=sqlalchemy.String)
    )
    optional_int: Mapped[Optional[int]] = mapped_column(nullable=True)
    sqla_tag_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey(SQLATag.id))
    sqla_tag: Mapped[Optional[SQLATag]] = relationship()
    labels: Mapped[List[SQLALabel]] = relationship(back_populates="test_dataclass")
    # do not use lower case dict here!
    # https://github.com/sqlalchemy/sqlalchemy/issues/9902
    dict_str_str: Mapped[Dict[str, str]] = mapped_column()
    default_factory: Mapped[List[int]] = mapped_column(
        sqlalchemy.types.ARRAY(item_type=sqlalchemy.INTEGER),
        default_factory=list,
    )
    __tablename__: str = "test_dataclass"

    @property
    def str_property(self) -> str:
        """String property.

        Returns:
            Name attribute
        """
        return self.name

    @hybrid_property
    def str_or_int_property(self) -> Union[str, int]:
        """String or int property.

        Returns:
            Name attribute
        """
        return self.name

    @hybrid_property
    def first_label(self) -> Optional[SQLALabel]:
        """First label property.

        Returns:
            First label
        """
        return self.labels[0] if self.labels else None


class ModelClass(rx.Model):
    """Test reflex model."""

    no_default: Optional[int] = sqlmodel.Field(nullable=True)
    count: int = 0
    name: str = "test"
    int_list: List[int] = []
    str_list: List[str] = []
    optional_int: Optional[int] = None
    sqla_tag: Optional[SQLATag] = None
    labels: List[SQLALabel] = []
    dict_str_str: Dict[str, str] = {}
    default_factory: List[int] = sqlmodel.Field(default_factory=list)

    @property
    def str_property(self) -> str:
        """String property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def str_or_int_property(self) -> Union[str, int]:
        """String or int property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def first_label(self) -> Optional[SQLALabel]:
        """First label property.

        Returns:
            First label
        """
        return self.labels[0] if self.labels else None


class BaseClass(rx.Base):
    """Test rx.Base class."""

    no_default: Optional[int] = pydantic.v1.Field(required=False)
    count: int = 0
    name: str = "test"
    int_list: List[int] = []
    str_list: List[str] = []
    optional_int: Optional[int] = None
    sqla_tag: Optional[SQLATag] = None
    labels: List[SQLALabel] = []
    dict_str_str: Dict[str, str] = {}
    default_factory: List[int] = pydantic.v1.Field(default_factory=list)

    @property
    def str_property(self) -> str:
        """String property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def str_or_int_property(self) -> Union[str, int]:
        """String or int property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def first_label(self) -> Optional[SQLALabel]:
        """First label property.

        Returns:
            First label
        """
        return self.labels[0] if self.labels else None


class BareClass:
    """Bare python class."""

    count: int = 0
    name: str = "test"
    int_list: List[int] = []
    str_list: List[str] = []
    optional_int: Optional[int] = None
    sqla_tag: Optional[SQLATag] = None
    labels: List[SQLALabel] = []
    dict_str_str: Dict[str, str] = {}

    @property
    def str_property(self) -> str:
        """String property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def str_or_int_property(self) -> Union[str, int]:
        """String or int property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def first_label(self) -> Optional[SQLALabel]:
        """First label property.

        Returns:
            First label
        """
        return self.labels[0] if self.labels else None


@attrs.define
class AttrClass:
    """Test attrs class."""

    count: int = 0
    name: str = "test"
    int_list: List[int] = []
    str_list: List[str] = []
    optional_int: Optional[int] = None
    sqla_tag: Optional[SQLATag] = None
    labels: List[SQLALabel] = []
    dict_str_str: Dict[str, str] = {}
    default_factory: List[int] = attrs.field(factory=list)

    @property
    def str_property(self) -> str:
        """String property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def str_or_int_property(self) -> Union[str, int]:
        """String or int property.

        Returns:
            Name attribute
        """
        return self.name

    @property
    def first_label(self) -> Optional[SQLALabel]:
        """First label property.

        Returns:
            First label
        """
        return self.labels[0] if self.labels else None


@pytest.mark.parametrize(
    "cls",
    [
        SQLAClass,
        SQLAClassDataclass,
        BaseClass,
        BareClass,
        ModelClass,
        AttrClass,
    ],
)
@pytest.mark.parametrize(
    "attr, expected",
    [
        pytest.param("count", int, id="int"),
        pytest.param("name", str, id="str"),
        pytest.param("int_list", List[int], id="List[int]"),
        pytest.param("str_list", List[str], id="List[str]"),
        pytest.param("optional_int", Optional[int], id="Optional[int]"),
        pytest.param("sqla_tag", Optional[SQLATag], id="Optional[SQLATag]"),
        pytest.param("labels", List[SQLALabel], id="List[SQLALabel]"),
        pytest.param("dict_str_str", Dict[str, str], id="Dict[str, str]"),
        pytest.param("str_property", str, id="str_property"),
        pytest.param("str_or_int_property", Union[str, int], id="str_or_int_property"),
        pytest.param("first_label", Optional[SQLALabel], id="first_label"),
    ],
)
def test_get_attribute_access_type(cls: type, attr: str, expected: GenericType) -> None:
    """Test get_attribute_access_type returns the correct type.

    Args:
        cls: Class to test.
        attr: Attribute to test.
        expected: Expected type.
    """
    assert get_attribute_access_type(cls, attr) == expected


@pytest.mark.parametrize(
    "cls",
    [
        SQLAClassDataclass,
        BaseClass,
        ModelClass,
        AttrClass,
    ],
)
def test_get_attribute_access_type_default_factory(cls: type) -> None:
    """Test get_attribute_access_type returns the correct type for default factory fields.

    Args:
        cls: Class to test.
    """
    assert get_attribute_access_type(cls, "default_factory") == List[int]


@pytest.mark.parametrize(
    "cls",
    [
        SQLAClassDataclass,
        BaseClass,
        ModelClass,
    ],
)
def test_get_attribute_access_type_no_default(cls: type) -> None:
    """Test get_attribute_access_type returns the correct type for fields with no default which are not required.

    Args:
        cls: Class to test.
    """
    assert get_attribute_access_type(cls, "no_default") == Optional[int]
