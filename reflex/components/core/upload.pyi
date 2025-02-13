"""Stub file for reflex/components/core/upload.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from pathlib import Path
from typing import Any, ClassVar, Dict, List, Optional, Union, overload

from reflex.components.base.fragment import Fragment
from reflex.components.component import Component, ComponentNamespace, MemoizationLeaf
from reflex.constants import Dirs
from reflex.event import CallableEventSpec, EventSpec, EventType
from reflex.style import Style
from reflex.utils.imports import ImportVar
from reflex.vars import VarData
from reflex.vars.base import Var

DEFAULT_UPLOAD_ID: str
upload_files_context_var_data: VarData

def upload_file(id_: str = DEFAULT_UPLOAD_ID) -> Var: ...
def selected_files(id_: str = DEFAULT_UPLOAD_ID) -> Var: ...
@CallableEventSpec
def clear_selected_files(id_: str = DEFAULT_UPLOAD_ID) -> EventSpec: ...
def cancel_upload(upload_id: str) -> EventSpec: ...
def get_upload_dir() -> Path: ...

uploaded_files_url_prefix = Var(
    _js_expr="getBackendURL(env.UPLOAD)",
    _var_data=VarData(
        imports={
            f"$/{Dirs.STATE_PATH}": "getBackendURL",
            "$/env.json": ImportVar(tag="env", is_default=True),
        }
    ),
).to(str)

def get_upload_url(file_path: str) -> Var[str]: ...

class UploadFilesProvider(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "UploadFilesProvider":
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class GhostUpload(Fragment):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_drop: Optional[Union[EventType[()], EventType[Any]]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "GhostUpload":
        """Create the component.

        Args:
            *children: The children of the component.
            on_drop: Fired when files are dropped.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class Upload(MemoizationLeaf):
    is_used: ClassVar[bool] = False

    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        accept: Optional[Union[Dict[str, List], Var[Optional[Dict[str, List]]]]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_files: Optional[Union[Var[int], int]] = None,
        max_size: Optional[Union[Var[int], int]] = None,
        min_size: Optional[Union[Var[int], int]] = None,
        multiple: Optional[Union[Var[bool], bool]] = None,
        no_click: Optional[Union[Var[bool], bool]] = None,
        no_drag: Optional[Union[Var[bool], bool]] = None,
        no_keyboard: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_drop: Optional[Union[EventType[()], EventType[Any]]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "Upload":
        """Create an upload component.

        Args:
            *children: The children of the component.
            accept: The list of accepted file types. This should be a dictionary of MIME types as keys and array of file formats as  values.  supported MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            disabled: Whether the dropzone is disabled.
            max_files: The maximum number of files that can be uploaded.
            max_size: The maximum file size (bytes) that can be uploaded.
            min_size: The minimum file size (bytes) that can be uploaded.
            multiple: Whether to allow multiple files to be uploaded.
            no_click: Whether to disable click to upload.
            no_drag: Whether to disable drag and drop.
            no_keyboard: Whether to disable using the space/enter keys to upload.
            on_drop: Fired when files are dropped.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The upload component.
        """
        ...

class StyledUpload(Upload):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        accept: Optional[Union[Dict[str, List], Var[Optional[Dict[str, List]]]]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_files: Optional[Union[Var[int], int]] = None,
        max_size: Optional[Union[Var[int], int]] = None,
        min_size: Optional[Union[Var[int], int]] = None,
        multiple: Optional[Union[Var[bool], bool]] = None,
        no_click: Optional[Union[Var[bool], bool]] = None,
        no_drag: Optional[Union[Var[bool], bool]] = None,
        no_keyboard: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_drop: Optional[Union[EventType[()], EventType[Any]]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "StyledUpload":
        """Create the styled upload component.

        Args:
            *children: The children of the component.
            accept: The list of accepted file types. This should be a dictionary of MIME types as keys and array of file formats as  values.  supported MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            disabled: Whether the dropzone is disabled.
            max_files: The maximum number of files that can be uploaded.
            max_size: The maximum file size (bytes) that can be uploaded.
            min_size: The minimum file size (bytes) that can be uploaded.
            multiple: Whether to allow multiple files to be uploaded.
            no_click: Whether to disable click to upload.
            no_drag: Whether to disable drag and drop.
            no_keyboard: Whether to disable using the space/enter keys to upload.
            on_drop: Fired when files are dropped.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The styled upload component.
        """
        ...

class UploadNamespace(ComponentNamespace):
    root = Upload.create

    @staticmethod
    def __call__(
        *children,
        accept: Optional[Union[Dict[str, List], Var[Optional[Dict[str, List]]]]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_files: Optional[Union[Var[int], int]] = None,
        max_size: Optional[Union[Var[int], int]] = None,
        min_size: Optional[Union[Var[int], int]] = None,
        multiple: Optional[Union[Var[bool], bool]] = None,
        no_click: Optional[Union[Var[bool], bool]] = None,
        no_drag: Optional[Union[Var[bool], bool]] = None,
        no_keyboard: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_drop: Optional[Union[EventType[()], EventType[Any]]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "StyledUpload":
        """Create the styled upload component.

        Args:
            *children: The children of the component.
            accept: The list of accepted file types. This should be a dictionary of MIME types as keys and array of file formats as  values.  supported MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            disabled: Whether the dropzone is disabled.
            max_files: The maximum number of files that can be uploaded.
            max_size: The maximum file size (bytes) that can be uploaded.
            min_size: The minimum file size (bytes) that can be uploaded.
            multiple: Whether to allow multiple files to be uploaded.
            no_click: Whether to disable click to upload.
            no_drag: Whether to disable drag and drop.
            no_keyboard: Whether to disable using the space/enter keys to upload.
            on_drop: Fired when files are dropped.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The styled upload component.
        """
        ...

upload = UploadNamespace()
