from django.shortcuts import render
from django.http import HttpResponse
from .utils import ordinal_number

def likelion_shield_badge(request):
  generation = request.GET.get('generation') or 9

  svg = '''
    <svg height="20" width="110" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41 8.1">
      <defs>
        <style>
          .cls-1 {{
            fill:#231815;
          }}
          .cls-2 {{
            font-size:6px;
            font-family:GillSans-SemiBold,Gill Sans;
            font-weight:600;
          }}
          .cls-2,.cls-3 {{
            fill:#f39800;
          }}
        </style>
      </defs>
      <g id="레이어_2" data-name="레이어 2">
        <g id="레이어_1-2" data-name="레이어 1">
          <rect class="cls-1" width="41" height="8.1" rx="1.44"/>
          <text class="cls-2" transform="translate(1.52 5.86)">
            LikeLion
          </text>
          <rect class="cls-3" x="26.2" y="1.55" width="0.3" height="5.0"/>
          <text class="cls-2" text-anchor="middle" transform="translate(33 5.92)">
            {generation_ordinal_number}
          </text>
        </g>
      </g>
    </svg>'''.format(
      generation_ordinal_number=ordinal_number(generation),
    )

  response = HttpResponse(content=svg)
  response['Content-Type'] = 'image/svg+xml'
  response['Cache-Control'] = 'no-cache'
  return response
