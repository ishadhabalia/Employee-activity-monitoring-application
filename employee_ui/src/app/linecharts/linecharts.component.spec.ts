import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinechartsComponent } from './linecharts.component';

describe('LinechartsComponent', () => {
  let component: LinechartsComponent;
  let fixture: ComponentFixture<LinechartsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LinechartsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LinechartsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
