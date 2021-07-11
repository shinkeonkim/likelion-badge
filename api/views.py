from django.shortcuts import render
from django.http import HttpResponse
from .utils import ordinal_number

def likelion_shield_badge(request):
  generation = request.GET.get('generation') or 9

  svg = '''
  <svg height="20" width="110" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 103.37 20">
    <defs>
      <style>
        .cls-1,.cls-4 {{
          fill:#231815;
        }}
        .cls-2 {{
          isolation:isolate;
        }}
        .cls-2,.cls-4 {{
          font-size:14.81px;font-family:GillSans-SemiBold, Gill Sans;font-weight:600;
        }}
        .cls-2,.cls-3 {{
          fill:#f39800; 
        }}
      </style>
    </defs>
    <g id="레이어_2" data-name="레이어 2">
      <g id="레이어_1-2" data-name="레이어 1">
        <g id="레이어_1-2-2" data-name="레이어 1-2">
          <rect class="cls-1" width="103.37" height="20" rx="3.63" />
          <text class="cls-2" transform="translate(5.67 14.47)">
            LikeLion
          </text>
          <path class="cls-3" d="M67.3, 0H99.74a3.59, 3.59, 0, 0, 1, 3.63, 3.56V16.44A3.59, 3.59, 0, 0, 1, 99.74, 20H67.3"/>
          <text class="cls-4" text-anchor="middle" transform="translate(83.49 14.47)">
            {generation_ordinal_number}
          </text>
        </g>
      </g>
    </g>
  </svg>'''.format(
      generation_ordinal_number=ordinal_number(generation),
    )

  response = HttpResponse(content=svg)
  response['Content-Type'] = 'image/svg+xml'
  response['Cache-Control'] = 'no-cache'
  return response
