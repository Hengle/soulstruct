from __future__ import annotations

__all__ = ["OBJ_ACT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import ObjActSuccessCondition


# noinspection PyDataclass
@dataclass(slots=True)
class OBJ_ACT_PARAM_ST(ParamRowData):
    PromptMessage: EventText = ParamField(
        int, "actionEnableMsgId", default=-1,
        tooltip="Message displayed in dialog box that prompts action (e.g. 'Open').",
    )
    FailureMessage: EventText = ParamField(
        int, "actionFailedMsgId", default=-1,
        tooltip="Message displayed in dialog box upon failed action (e.g. 'It's locked').",
    )
    FlagForAutomaticSuccess: Flag = ParamField(
        int, "spQualifiedPassEventFlag", default=-1,
        tooltip="Action will always be successful if this flag is enabled.",
    )
    PlayerActionAnimation: int = ParamField(
        uint, "playerAnimId", default=0,
        tooltip="Animation played by a player character when they successfully activate the object.",
    )
    NonPlayerActionAnimation: int = ParamField(
        uint, "chrAnimId", default=0,
        tooltip="Animation played by a non-player character when they successfully activate the object.",
    )
    MaxActionDistance: int = ParamField(
        ushort, "validDist", default=150,
        tooltip="Maximum distance from action model point at which the object action will be prompted.",
    )
    spQualifiedId: ushort = ParamField(
        ushort, "spQualifiedId", default=0, dynamic_callback=ObjActSuccessCondition(1),
        tooltip="TODO",
    )
    spQualifiedId2: ushort = ParamField(
        ushort, "spQualifiedId2", default=0, dynamic_callback=ObjActSuccessCondition(2),
        tooltip="TODO",
    )
    ObjectActionModelPoint: int = ParamField(
        byte, "objDummyId", default=0,
        tooltip="Model point that specifies where the action occurs on the object (for snapping the player and "
                "distance check).",
    )
    _Pad0: bytes = ParamPad(1, "pad0[1]")
    ObjectActionAnimation: int = ParamField(
        uint, "objAnimId", default=0,
        tooltip="Animation played by the object when it is successfully activated.",
    )
    MaxPlayerAngle: int = ParamField(
        byte, "validPlayerAngle", default=30,
        tooltip="Maximum angle between the character's forward direction and the direction to the object action point "
                "for the action prompt to appear.",
    )
    SuccessCondition1Type: OBJACT_SP_QUALIFIED_TYPE = ParamField(
        byte, "spQualifiedType", default=0,
        tooltip="Type of first success condition.",
    )
    SuccessCondition2Type: OBJACT_SP_QUALIFIED_TYPE = ParamField(
        byte, "spQualifiedType2", default=0,
        tooltip="Type of second success condition.",
    )
    MaxObjectAngle: int = ParamField(
        byte, "validObjAngle", default=30,
        tooltip="Maximum angle between the object's forward direction and the direction to the player for the action "
                "prompt to appear.",
    )
    CharacterSnapType: OBJACT_CHR_SORB_TYPE = ParamField(
        byte, "chrSorbType", default=0,
        tooltip="Type of method used to snap the character to the object before animations are played.",
    )
    EventTriggerDelay: int = ParamField(
        byte, "eventKickTiming", default=0,
        tooltip="I believe this is the delay between successful object activation and the outgoing 'success' trigger "
                "used by game events.",
    )
    _Pad1: bytes = ParamPad(2, "pad1[2]")
    ActionButtonParamID: int = ParamField(
        int, "actionButtonParamId", default=-1,
        tooltip="TODO",
    )
    ActionSuccessMessageID: EventText = ParamField(
        int, "actionSuccessMsgId", default=-1,
        tooltip="TODO",
    )
