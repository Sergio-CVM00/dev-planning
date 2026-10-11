# Boardroom project evidence

This is a synthetic existing-product fixture. No product code or live services are supplied.

## Product and current behavior

Boardroom is a web application for shared project boards. A signed-in user selects one team. Team roles are owner and member. Owners currently manage membership through a support request; there is no invitation flow. Users may belong to several teams. Team data must not be visible to nonmembers. The owner has not decided which team roles may send invitations.

The requested feature is a durable team invitation, accepted by a signed-in account matching its target email. An invitation must not disclose the team's boards before acceptance. Email delivery and reminders are outside this first feature; people share an invitation link themselves.

## Current contracts and environment

The web client calls the existing authenticated HTTP interface. Server handlers receive user identity and selected team; permission enforcement must be server-side. PostgreSQL stores users, teams, and memberships. Membership has a unique (team_id, user_id) constraint. There is no invitation table.

The documented CI harness supports API integration checks with a disposable PostgreSQL fixture and a web journey runner. A future run can create two teams, owners, members, and a signed-in nonmember. No executable harness or runtime access is included in this planning fixture. Test execution is not authorized here.

Reuse the current web design system and authenticated request boundary. This planning exercise has no external issue tracker. Saved English Markdown under planning/ is the authoritative output; a visual or human summary must link those records. No canonical JSON requirement applies to this fixture.

## Constraints

Invitation expiration is 24 hours from creation, tokens are single-use, and the first slice must survive a reload and server restart. Concurrent acceptance must not duplicate membership. Do not plan email-provider integration, billing, or production deployment. Avoid adding an orchestration framework.
