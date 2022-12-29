# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/argoproj/argo-workflows/master/api/openapi-spec/swagger.json
#   timestamp: 2022-12-29T22:26:11+00:00

from __future__ import annotations

from typing import Annotated, Optional

from pydantic import Field

from hera import ArgoBaseModel

from .io.argoproj.events import v1alpha1
from .io.k8s.apimachinery.pkg.apis.meta import v1


class DeleteSensorResponse(ArgoBaseModel):
    pass


class LogEntry(ArgoBaseModel):
    dependency_name: Annotated[
        Optional[str], Field(alias='dependencyName', title='optional - trigger dependency name')
    ] = None
    event_context: Annotated[Optional[str], Field(alias='eventContext', title='optional - Cloud Event context')] = None
    level: Optional[str] = None
    msg: Optional[str] = None
    namespace: Optional[str] = None
    sensor_name: Annotated[Optional[str], Field(alias='sensorName')] = None
    time: Optional[v1.Time] = None
    trigger_name: Annotated[Optional[str], Field(alias='triggerName', title='optional - any trigger name')] = None


class CreateSensorRequest(ArgoBaseModel):
    create_options: Annotated[Optional[v1.CreateOptions], Field(alias='createOptions')] = None
    namespace: Optional[str] = None
    sensor: Optional[v1alpha1.Sensor] = None


class SensorWatchEvent(ArgoBaseModel):
    object: Optional[v1alpha1.Sensor] = None
    type: Optional[str] = None


class UpdateSensorRequest(ArgoBaseModel):
    name: Optional[str] = None
    namespace: Optional[str] = None
    sensor: Optional[v1alpha1.Sensor] = None
