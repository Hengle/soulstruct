__all__ = [
    # Names processed directly by EVS parser
    "NeverRestart",
    "RestartOnRest",
    "UnknownRestart",
    "EVENTS",
    "Condition",
    "HeldCondition",
    "END",
    "RESTART",
    "Await",
    # Shared tests
    "THIS_FLAG",
    "THIS_SLOT_FLAG",
    "ONLINE",
    "OFFLINE",
    "DLC_OWNED",
    "SKULL_LANTERN_ACTIVE",
    "WHITE_WORLD_TENDENCY",
    "BLACK_WORLD_TENDENCY",
    "NEW_GAME_CYCLE",
    "PLAYER_LEVEL",
    "FlagEnabled",
    "FlagDisabled",
    "SecondsElapsed",
    "FramesElapsed",
    "CharacterInsideRegion",
    "CharacterOutsideRegion",
    "PlayerInsideRegion",
    "PlayerOutsideRegion",
    "AllPlayersInsideRegion",
    "AllPlayersOutsideRegion",
    "InsideMap",
    "OutsideMap",
    "EntityWithinDistance",
    "EntityBeyondDistance",
    "PlayerWithinDistance",
    "PlayerBeyondDistance",
    "HasItem",
    "HasWeapon",
    "HasArmor",
    "HasAccessory",
    "HasGood",
    "ActionButton",
    "MultiplayerEvent",
    "TrueFlagCount",
    "EventValue",
    "EventFlagValue",
    "AnyItemDroppedInRegion",
    "ItemDropped",
    "OwnsItem",
    "OwnsWeapon",
    "OwnsArmor",
    "OwnsAccessory",
    "OwnsGood",
    "Alive",
    "Dead",
    "Attacked",
    "HealthRatio",
    "HealthValue",
    "PartHealthValue",
    "IsCharacterType",
    "IsHollow",
    "IsHuman",
    "IsInvader",
    "IsBlackPhantom",
    "IsWhitePhantom",
    "HasSpecialEffect",
    "BackreadEnabled",
    "BackreadDisabled",
    "CharacterHasTAEEvent",
    "CharacterTargeting",
    "HasAIStatus",
    "HasNormalAIStatus",
    "HasRecognitionAIStatus",
    "HasAlertAIStatus",
    "HasBattleAIStatus",
    "PlayerIsClass",
    "PlayerInCovenant",
    "ObjectDamaged",
    "ObjectDestroyed",
    "ObjectActivated",
    "PlayerStandingOnCollision",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    # Dark Souls 3 tests
    "HOST",
    "CLIENT",
    "IN_OWN_WORLD",
    "ActionButtonParamActivated",
    "AttackedWithDamageType",
    "CharacterDrawGroupActive",
    "CharacterDrawGroupInactive",
]

from soulstruct.base.events.emevd.tests import *
from soulstruct.base.events.emevd.utils import no_skip_or_negate_or_return, ConstantCondition
from soulstruct.game_types import *
from . import instructions as instr
from .enums import *


HOST = ConstantCondition(
    if_true_func=instr.IfHost,
    skip_if_true_func=instr.SkipLinesIfHost,
    end_if_true_func=instr.EndIfHost,
    restart_if_true_func=instr.RestartIfHost,
)

CLIENT = ConstantCondition(
    if_true_func=instr.IfClient,
    skip_if_true_func=instr.SkipLinesIfClient,
    end_if_true_func=instr.EndIfClient,
    restart_if_true_func=instr.RestartIfClient,
)

IN_OWN_WORLD = ConstantCondition(
    if_true_func=instr.IfPlayerInOwnWorld,
    if_false_func=instr.IfPlayerNotInOwnWorld,
    end_if_true_func=instr.EndIfPlayerInOwnWorld,
    end_if_false_func=instr.EndIfPlayerNotInOwnWorld,
    restart_if_true_func=instr.RestartIfPlayerInOwnWorld,
    restart_if_false_func=instr.RestartIfPlayerNotInOwnWorld,
)


@no_skip_or_negate_or_return
def ActionButtonParamActivated(action_button_id: int, entity: CoordEntityTyping, condition: int):
    return instr.IfActionButtonParamActivated(condition, action_button_id, entity)


@no_skip_or_negate_or_return
def AttackedWithDamageType(
    attacked_entity: AnimatedEntityTyping, attacker: CharacterTyping, damage_type: DamageType, condition: int
):
    return instr.IfAttackedWithDamageType(condition, attacked_entity, attacker, damage_type)


@no_skip_or_negate_or_return
def CharacterDrawGroupActive(character: CharacterTyping, condition: int):
    return instr.IfCharacterDrawGroupActive(condition, character)


@no_skip_or_negate_or_return
def CharacterDrawGroupInactive(character: CharacterTyping, condition: int):
    return instr.IfCharacterDrawGroupInactive(condition, character)