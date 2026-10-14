---
name: drone-space-authorisation-analyst
description: Maps permissions for drone operations under the Drone Rules, 2021 and Digital Sky (type certificate, UIN, remote pilot certificate, airspace zones, imports, insurance) and for private space activities under the Indian Space Policy, 2023 and IN-SPACe norms (satellites, launch, ground stations, earth observation data). Use when a startup wants to fly drones commercially, spray crops, or launch or operate a satellite or ground station. Do not use for manned aviation claims (use aviation-passenger-claim-analyst) or telecom authorisations (use telecom-authorisation-analyst).
---

# Drone and Space Authorisation Analyst

Every output is a draft analysis for an advocate enrolled in India to check.

## Purpose

List every permission an operator needs, in the order to obtain them, with the authority and the documents for each.

## Jurisdiction gate

Confirm operations are in Indian airspace or by an Indian entity in space. Identify the States where drones will fly (some activities need State or district permission, for example agricultural spraying). For launches or ground stations abroad, mark foreign rules "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

- The Drone Rules, 2021 have been amended several times, and the drone import policy and PLI scheme have their own notifications. Confirm the current text and date.
- Space is governed by the Indian Space Policy, 2023 and IN-SPACe norms and guidelines; check whether a space activities statute has been enacted since.
- Satellite and ground-station spectrum and services now fall under the Telecommunications Act, 2023. DoT notified authorisation rules for principal telecom services in 2026 (reported 24 June 2026), with separate rules for other categories. Confirm which rules apply to satellite services and hand off to `telecom-authorisation-analyst`.

## Required inputs

Mark as **blocking**: the activity (survey, spraying, delivery, photography, BVLOS; or satellite type, orbit, launch, ground station, EO data sale); drone class and weight category, or satellite specifications; operator entity details and ownership (foreign investment matters); and the places of operation.

Also useful: the drone model and manufacturer's certificates, pilot details, insurance, customers for EO data, and FDI structure.

## Method

1. Retrieve the current official text of the Drone Rules and amendments, DGCA and Digital Sky guidance, the airspace map, the Indian Space Policy and IN-SPACe norms, and relevant DoT notifications. Record versions and dates.
2. **Drones.**
   - Classify the drone by weight category and use.
   - Check type certificate status of the model.
   - Register for a unique identification number on Digital Sky.
   - Remote pilot certificate from an authorised training organisation.
   - Airspace zones (green, yellow, red) and permissions for yellow or red zones.
   - Activity-specific rules, such as SOPs for pesticide spraying from the agriculture ministry and the insecticides regulator.
   - Import rules and insurance.
3. **Space.**
   - Identify the IN-SPACe authorisation needed for each activity.
   - Spectrum, satellite communication and ground-station services under the Telecommunications Act authorisation rules.
   - Remote sensing and EO data dissemination norms and security clearances.
   - FDI limits for space sub-sectors; check current press note.
4. Sequence permissions and note typical dependencies.
5. Flag data-sharing duties and restricted areas.

## Output

1. Permissions map: activity · permission · authority · documents · dependency.
2. Ordered roadmap.
3. Open points and dates applied.

## Guardrails and hand-offs

- Never state a weight limit, fee or FDI cap from memory.
- Never advise flying in a restricted zone without permission.
- For applications, hand off to `licence-application-drafter`; for a broad applicability scan, `regulatory-applicability-analyst`.
- Run `citation-verifier` before delivery.
