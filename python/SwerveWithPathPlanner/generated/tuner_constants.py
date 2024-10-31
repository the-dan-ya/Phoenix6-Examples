from phoenix6 import CANBus, configs, swerve, units
from subsystems.command_swerve_drivetrain import CommandSwerveDrivetrain
from wpimath.units import inchesToMeters


class TunerConstants:
    """
    Generated by the Tuner X Swerve Project Generator
    https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/tuner-swerve/index.html
    """

    # Both sets of gains need to be tuned to your individual robot

    # The steer motor uses any SwerveModule.SteerRequestType control request with the
    # output type specified by SwerveModuleConstants.SteerMotorClosedLoopOutput
    _steer_gains = (
        configs.Slot0Configs()
        .with_k_p(100)
        .with_k_i(0)
        .with_k_d(2.0)
        .with_k_s(0.2)
        .with_k_v(1.5)
        .with_k_a(0)
    )
    # When using closed-loop control, the drive motor uses the control
    # output type specified by SwerveModuleConstants.DriveMotorClosedLoopOutput
    _drive_gains = (
        configs.Slot0Configs()
        .with_k_p(0.1)
        .with_k_i(0)
        .with_k_d(0)
        .with_k_s(0)
        .with_k_v(0.12)
    )

    # The closed-loop output type to use for the steer motors;
    # This affects the PID/FF gains for the steer motors
    _steer_closed_loop_output = swerve.ClosedLoopOutputType.VOLTAGE
    # The closed-loop output type to use for the drive motors;
    # This affects the PID/FF gains for the drive motors
    _drive_closed_loop_output = swerve.ClosedLoopOutputType.VOLTAGE

    # The remote sensor feedback type to use for the steer motors;
    # When not Pro-licensed, FusedCANcoder/SyncCANcoder automatically fall back to RemoteCANcoder
    _steer_feedback_type = swerve.SteerFeedbackType.FUSED_CANCODER

    # The stator current at which the wheels start to slip;
    # This needs to be tuned to your individual robot
    _slip_current: units.ampere = 120.0

    # Initial configs for the drive and steer motors and the CANcoder; these cannot be null.
    # Some configs will be overwritten; check the `with_*_initial_configs()` API documentation.
    _drive_initial_configs = configs.TalonFXConfiguration()
    _steer_initial_configs = configs.TalonFXConfiguration().with_current_limits(
        configs.CurrentLimitsConfigs()
        # Swerve azimuth does not require much torque output, so we can set a relatively low
        # stator current limit to help avoid brownouts without impacting performance.
        .with_stator_current_limit(60).with_stator_current_limit_enable(True)
    )
    _cancoder_initial_configs = configs.CANcoderConfiguration()
    # Configs for the Pigeon 2; leave this None to skip applying Pigeon 2 configs
    _pigeon_configs: configs.Pigeon2Configuration | None = None

    # Theoretical free speed (m/s) at 12 V applied output;
    # This needs to be tuned to your individual robot
    speed_at_12_volts: units.meters_per_second = 4.70

    # Every 1 rotation of the azimuth results in _couple_ratio drive motor turns;
    # This may need to be tuned to your individual robot
    _couple_ratio = 3.5

    _drive_gear_ratio = 7.363636364
    _steer_gear_ratio = 12.8
    _wheel_radius: units.meter = inchesToMeters(2.167)

    _invert_left_side = False
    _invert_right_side = True

    _canbus = CANBus("rio", "./logs/example.hoot")
    _pigeon_id = 1

    # These are only used for simulation
    _steer_inertia: units.kilogram_square_meter = 0.00001
    _drive_inertia: units.kilogram_square_meter = 0.001
    # Simulated voltage necessary to overcome friction
    _steer_friction_voltage: units.volt = 0.25
    _drive_friction_voltage: units.volt = 0.25

    drivetrain_constants = (
        swerve.SwerveDrivetrainConstants()
        .with_can_bus_name(_canbus.name)
        .with_pigeon2_id(_pigeon_id)
        .with_pigeon2_configs(_pigeon_configs)
    )

    _constants_creator = (
        swerve.SwerveModuleConstantsFactory()
        .with_drive_motor_gear_ratio(_drive_gear_ratio)
        .with_steer_motor_gear_ratio(_steer_gear_ratio)
        .with_coupling_gear_ratio(_couple_ratio)
        .with_wheel_radius(_wheel_radius)
        .with_steer_motor_gains(_steer_gains)
        .with_drive_motor_gains(_drive_gains)
        .with_steer_motor_closed_loop_output(_steer_closed_loop_output)
        .with_drive_motor_closed_loop_output(_drive_closed_loop_output)
        .with_slip_current(_slip_current)
        .with_speed_at12_volts(speed_at_12_volts)
        .with_feedback_source(_steer_feedback_type)
        .with_drive_motor_initial_configs(_drive_initial_configs)
        .with_steer_motor_initial_configs(_steer_initial_configs)
        .with_cancoder_initial_configs(_cancoder_initial_configs)
        .with_steer_inertia(_steer_inertia)
        .with_drive_inertia(_drive_inertia)
        .with_steer_friction_voltage(_steer_friction_voltage)
        .with_drive_friction_voltage(_drive_friction_voltage)
    )

    # Front Left
    _front_left_drive_motor_id = 5
    _front_left_steer_motor_id = 4
    _front_left_encoder_id = 2
    _front_left_encoder_offset: units.rotation = -0.83544921875
    _front_left_steer_motor_inverted = True

    _front_left_x_pos: units.meter = inchesToMeters(10.5)
    _front_left_y_pos: units.meter = inchesToMeters(10.5)

    # Front Right
    _front_right_drive_motor_id = 7
    _front_right_steer_motor_id = 6
    _front_right_encoder_id = 3
    _front_right_encoder_offset: units.rotation = -0.15234375
    _front_right_steer_motor_inverted = True

    _front_right_x_pos: units.meter = inchesToMeters(10.5)
    _front_right_y_pos: units.meter = inchesToMeters(-10.5)

    # Back Left
    _back_left_drive_motor_id = 1
    _back_left_steer_motor_id = 0
    _back_left_encoder_id = 0
    _back_left_encoder_offset: units.rotation = -0.4794921875
    _back_left_steer_motor_inverted = True

    _back_left_x_pos: units.meter = inchesToMeters(-10.5)
    _back_left_y_pos: units.meter = inchesToMeters(10.5)

    # Back Right
    _back_right_drive_motor_id = 3
    _back_right_steer_motor_id = 2
    _back_right_encoder_id = 1
    _back_right_encoder_offset: units.rotation = -0.84130859375
    _back_right_steer_motor_inverted = True

    _back_right_x_pos: units.meter = inchesToMeters(-10.5)
    _back_right_y_pos: units.meter = inchesToMeters(-10.5)

    front_left = _constants_creator.create_module_constants(
        _front_left_steer_motor_id,
        _front_left_drive_motor_id,
        _front_left_encoder_id,
        _front_left_encoder_offset,
        _front_left_x_pos,
        _front_left_y_pos,
        _invert_left_side,
        _front_left_steer_motor_inverted,
    )
    front_right = _constants_creator.create_module_constants(
        _front_right_steer_motor_id,
        _front_right_drive_motor_id,
        _front_right_encoder_id,
        _front_right_encoder_offset,
        _front_right_x_pos,
        _front_right_y_pos,
        _invert_right_side,
        _front_right_steer_motor_inverted,
    )
    back_left = _constants_creator.create_module_constants(
        _back_left_steer_motor_id,
        _back_left_drive_motor_id,
        _back_left_encoder_id,
        _back_left_encoder_offset,
        _back_left_x_pos,
        _back_left_y_pos,
        _invert_left_side,
        _back_left_steer_motor_inverted,
    )
    back_right = _constants_creator.create_module_constants(
        _back_right_steer_motor_id,
        _back_right_drive_motor_id,
        _back_right_encoder_id,
        _back_right_encoder_offset,
        _back_right_x_pos,
        _back_right_y_pos,
        _invert_right_side,
        _back_right_steer_motor_inverted,
    )

    @classmethod
    def create_drivetrain(clazz) -> CommandSwerveDrivetrain:
        """
        Creates a CommandSwerveDrivetrain instance.
        This should only be called once in your robot program.
        """
        return CommandSwerveDrivetrain(
            clazz.drivetrain_constants,
            [
                clazz.front_left,
                clazz.front_right,
                clazz.back_left,
                clazz.back_right,
            ],
        )